from collections import OrderedDict
from sympy import *


class Processors:
    def __init__(self, groups):
        self.amount = sum(len(x) for x in groups)
        self.dict = OrderedDict()
        for i in range(1, self.amount + 1):
            self.dict['x' + str(i)] = True


    def generate_combinations(self, faults_list):
        self.set_true()
        for i in faults_list:
            self.dict[i] = False

    def set_true(self):
        for i in self.dict:
            self.dict[i] = True

    def divide_processors(self, amounts, processors_dictionary):
        divided_processors = []
        divided_processors.append(list(processors_dictionary[:amounts[0]]))
        divided_processors.append(list(processors_dictionary[amounts[0]:]))
        return divided_processors

    def form_groups_according_to_blocked_vector(self, blocked_vector):
        return [list(set(self.dict.keys()) - set(blocked_vector)), [blocked_vector]]

        # def get_required_processors(self, required_processors):
        # return dict(zip(required_processors.keys(), [self.dict[k] for k in required_processors.keys()]))

        # def get_sympy_array(self, dictionary):
        # return symbols(dictionary)

