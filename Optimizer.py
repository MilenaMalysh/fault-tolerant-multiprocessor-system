import itertools
from sympy.simplify.cse_main import cse
from sympy.parsing.sympy_parser import parse_expr
from sympy import *


class Optimizer:
    def __init__(self, fault_tolerance, processors, optimized_file):
        self.concatenated_formulas = []
        self.result_formulas = []
        self.amount_processor = processors.amount
        self.fault_tolerance = fault_tolerance
        self.processors = processors
        self.optimized_file = optimized_file

    def optimize(self, original_formulas):

        self.form_formulas(original_formulas)
        table1 = self.form_table(self.fault_tolerance)
        table2 = self.form_table(self.fault_tolerance + 1)
        self.result_formulas = self.choose_result_formulas(table1, table2)
        with open(self.optimized_file, "w") as f:
            for i in self.result_formulas:
                f.write("\n Next combination of formulas:")
                f.write("\n".join("%s " % x for x in i))
        f.close()

    def check_amount(self, comb, table, null_amount):
        for i in itertools.combinations(self.processors.dict.keys(), null_amount):
            amount = 0
            for formula in comb:
                if not table[formula, i]:
                    amount += 1
            if null_amount == self.fault_tolerance:
                if amount > 1:
                    return False
            else:
                if amount < 2:
                    return False
        return True


    def choose_result_formulas(self, table1, table2):
        itr = 1
        lst_combinations = []
        while True:
            flag = False
            for comb in itertools.combinations(self.concatenated_formulas, itr):
                if self.check_amount(comb, table1, self.fault_tolerance) and self.check_amount(comb, table2,
                                                                                               self.fault_tolerance + 1):
                    flag = True
                    lst_combinations.append(comb)
            itr += 1
            if itr == len(self.concatenated_formulas) + 1 or flag:
                break
        return lst_combinations


    def form_table(self, null_amount):
        combinations = itertools.combinations(self.processors.dict.keys(), null_amount)
        table = {}
        for i in combinations:
            self.processors.generate_combinations(i)
            for j in self.concatenated_formulas:
                table[j, i] = j.subs(self.processors.dict)
        return table

    def form_formulas(self, original_formulas):
        for itr in range(2, len(original_formulas)):
            for comb in itertools.combinations(original_formulas, itr):
                formula = self.check_comb_formulas(comb)
                if formula:
                    self.concatenated_formulas.append(formula)

        while True:
            flag = True
            for itr in range(len(self.concatenated_formulas), 1, -1):
                for comb in itertools.combinations(list(self.concatenated_formulas), itr):
                    formula = self.check_comb_formulas(comb)
                    if formula:
                        flag = False
                        self.concatenated_formulas = list(set(self.concatenated_formulas) - set(comb))
                        self.concatenated_formulas.append(formula)
                        break
                else:
                    continue
                break
            if flag:
                break
        self.concatenated_formulas += original_formulas


    def check_comb_formulas(self, formulas):
        common = self.common_part(formulas)
        if common:
            formula = []
            for f in formulas:
                rest = Or(*filter(lambda x: x not in common, f.args))
                formula.append(rest)
            formula = Or(Or(*common), And(*formula))
            return formula


    def common_part(self, formulas):
        # for iter in range(len((parse_expr(min(formulas, key=len))).args), 0,-1):
        shortest_function = min(formulas, key=lambda x: len(x.args))
        for itr in range(len(shortest_function.args), 0, -1):
            for terms in itertools.combinations(formulas[0].args, itr):
                for formula in formulas:
                    for term in terms:
                        if term not in formula.args:
                            break
                    else:
                        continue  # executed if the loop ended normally (no break)
                    break
                else:
                    return terms





