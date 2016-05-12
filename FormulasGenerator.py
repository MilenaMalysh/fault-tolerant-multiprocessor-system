from collections import OrderedDict
import itertools
from sympy import *


class FormulasGenerator:
    def __init__(self, processors, fault_tolerance):
        self.origin_formulas_arr = []
        self.fault_tolerance = fault_tolerance
        self.processors = processors


    def generate(self, group_of_processors, outfile):

        with open(outfile, "w") as f:
            self.origin_formulas_arr = self.generate_formulas(self.fault_tolerance, self.processors.dict.keys(),
                                                              group_of_processors)
            f.write("\n".join("%s " % x for x in self.origin_formulas_arr))
        f.close()


    def generate_formulas(self, fault_tolerance, processors_dictionary, groups):
        formulas = []
        if fault_tolerance == 1:
            formula = And(*symbols(processors_dictionary))
            formulas.append(formula)
            return formulas

        elif fault_tolerance == len(processors_dictionary):
            formula = Or(*symbols(processors_dictionary))
            formulas.append(formula)
            return formulas

        else:
            faults_distributions = []
            for fault_combination in itertools.combinations(processors_dictionary, fault_tolerance):
                faults_distribution = self.count_combination(fault_combination, groups)
                if faults_distribution not in faults_distributions:
                    faults_distributions.append(self.count_combination(fault_combination, groups))
                    formulas_groups = []
                    for group in groups:
                        next_groups = self.processors.divide_processors(
                            [(len(group) / 2), (len(group) - len(group) / 2)], group)
                        if faults_distribution[groups.index(group)] != 0:
                            formulas_groups.append(
                                self.generate_formulas(faults_distribution[groups.index(group)], group, next_groups))
                    for v in itertools.product(*formulas_groups):
                        formulas.append(Or(*v))

            return formulas

    def count_combination(self, fault_combination, groups):
        self.processors.generate_combinations(fault_combination)
        count_combination = []
        for group in groups:
            fault_tolerance_for_group = 0
            for item in group:
                if not self.processors.dict.get(item):
                    fault_tolerance_for_group += 1
            count_combination.append(fault_tolerance_for_group)
        return count_combination



