from sympy.logic.boolalg import to_dnf
from sympy import *


class Selector:
    def __init__(self, blocked_vectors):
        self.blocked_vectors = blocked_vectors


    def select_group(self, formulas):
        selected =  min(self.select_max_contains(formulas),
                   key=lambda block: sum(len(to_dnf(formula).args) for formula in block))
        print "selected"
        for j in selected:
             print j
        print '\n'
        return selected


    def select_n_formulas(self, blocked_formulas, amount_of_formulas):
        return sorted(blocked_formulas, key=lambda formula: len(to_dnf(formula).args))[:amount_of_formulas]


    def select_max_contains(self, formulas):

        print "original"
        for i in formulas:
            for j in i:
                print j
            print '\n'

        max_cont = 0
        filtered_formulas = []
        for i in formulas:
            curr_cont = 0
            for formula in i:
                if any(formula.atoms() == set(symbols(vector)) for vector in self.blocked_vectors):
                    curr_cont += 1
            if curr_cont > max_cont:
                max_cont = curr_cont
                filtered_formulas = [i]
            elif curr_cont == max_cont:
                filtered_formulas.append(i)
        if not filtered_formulas:
            return formulas

        print "\n"
        print "selected"
        print "\n"

        for i in filtered_formulas:
            for j in i:
                print j
            print '\n'



        return filtered_formulas







