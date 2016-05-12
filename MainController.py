from Optimizer import Optimizer
from Processors import Processors
from Selector import Selector
from Blocker import Blocker
from PrTester import PrTester
from InputController import InputController
from FormulasGenerator import *
import sys


class MainController:
    def __init__(self):
        self.input_controller = InputController()
        self.original_formulas_file = sys.argv[1]
        self.researched_formulas_file = sys.argv[2]
        self.optimized_original_file = sys.argv[3]
        self.optimized_researched_file = sys.argv[4]
        self.result_of_testing_original_file = sys.argv[5]
        self.result_of_testing_researched_file = sys.argv[6]
        self.analyzer_results = sys.argv[7]


    def start(self):

        self.input_controller.fault_tolerance_request()
        self.input_controller.initial_groups_request()
        self.input_controller.blocked_vector_request()

        tested_faults = len(max(self.input_controller.initial_groups, key=len))

        processors = Processors(self.input_controller.initial_groups)
        generator = FormulasGenerator(processors, self.input_controller.fault_tolerance)
        selector = Selector(self.input_controller.blocked_vectors)
        tester = PrTester(processors)
        blocker = Blocker(self.input_controller.blocked_vectors, tester, selector, processors)


        '''
            For original formulas
        '''
        generator.generate(self.input_controller.initial_groups, self.original_formulas_file)
        optimizer_original = Optimizer(self.input_controller.fault_tolerance, processors, self.optimized_original_file)
        optimizer_original.optimize(generator.origin_formulas_arr)
        blocking_original_formulas = blocker.block_original(selector.select_group(optimizer_original.result_formulas))
        tester.test(self.result_of_testing_original_file, blocking_original_formulas, tested_faults, self.input_controller.fault_tolerance)

        '''
            For researched formulas
        '''
        self.input_controller.researched_way_request()
        if self.input_controller.researched_way:

            generator.generate(processors.form_groups_according_to_blocked_vector(self.input_controller.blocked_vectors), self.researched_formulas_file)
            optimizer_researched = Optimizer(self.input_controller.fault_tolerance, processors, self.optimized_researched_file)
            optimizer_researched.optimize(generator.origin_formulas_arr)
            #selector.select_group(optimizer_researched.result_formulas)
            blocking_researched_formulas = blocker.block_researched(selector.select_group(optimizer_researched.result_formulas))
            tester.test(self.result_of_testing_researched_file,blocking_researched_formulas, tested_faults, self.input_controller.fault_tolerance)




        self.input_controller.repeat_request()

        return self.input_controller.repeat
