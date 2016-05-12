from sympy import *


class Blocker:
    def __init__(self, blocked_vectors, tester, selector, processors):
        self.blocked_vectors = blocked_vectors
        self.tester = tester
        self.selector = selector
        self.processors = processors



    def block_original(self, formulas):
        blocked_formulas = list(formulas)
        for vector in self.blocked_vectors:
            nulled_formulas = self.tester.get_nulled(blocked_formulas, vector)
            selected_formulas = self.selector.select_n_formulas(blocked_formulas, len(nulled_formulas)-1)
            for n,i in enumerate(blocked_formulas):
                if i in selected_formulas:
                    blocked_formulas[n] = (Or(i, And(And(*symbols(filter(lambda x: x not in vector, self.processors.dict))), And(*map(lambda x: Not(symbols(x)), vector)))))


        return blocked_formulas

    def block_researched(self, formulas):
        blocked_formulas = list(formulas)
        for vector in self.blocked_vectors:
            nulled_formulas = self.tester.get_nulled(blocked_formulas, vector)
            selected_formulas = self.selector.select_n_formulas(blocked_formulas, len(nulled_formulas)-1)
            for n,i in enumerate(blocked_formulas):
                if i in selected_formulas:
                    blocked_formulas[n] = (Or(i, And(*symbols(filter(lambda x: x not in vector, self.processors.dict)))))


        return blocked_formulas





