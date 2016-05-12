import itertools
from sympy.parsing.sympy_parser import parse_expr


class PrTester:
    def __init__(self, processors):
        self.processors = processors




    def test(self, fileout, formulas, tested_faults, fault_tolerance):

        with open(fileout, 'w') as fileout:

            fileout.write('Formulas:\n')
            for f in formulas:
                fileout.write("%s \n" % f)

            fileout.write(" \n")

            for i in range(1, tested_faults + 1):
                fileout.write('%s fault(s)\n' % str(i))
                faults_combination = 0
                for j in itertools.combinations(self.processors.dict.keys(), i):

                                # fileout.write('%s \n' % formula)
                    if len(self.get_nulled(formulas, j)) >= 2:
                        faults_combination += 1
                    elif i > fault_tolerance:
                        fileout.write('Blocked vector: %s \n' % list(j))

                fileout.write(' %s combination failed from %s combinations \n' % (
                faults_combination, (len(list(itertools.combinations(self.processors.dict.keys(), i))))))



    def get_nulled(self, blocked_formulas, vector):

        self.processors.generate_combinations(vector)
        nulled_formulas = []
        for formula in blocked_formulas:
            if not formula.subs(self.processors.dict):
                nulled_formulas.append(formula)
        return nulled_formulas

    '''

    def test(self, fileout, formulas, tested_faults):
        comb_number = 1
        with open(fileout, 'w') as fileout:

            fileout.write('Formulas:\n')
            for f in formulas:
                fileout.write("%s \n" % f)

            fileout.write(" \n")
            for variant in formulas:
                fileout.write("%s)" % comb_number)
                for formula in variant:
                    fileout.write("%s \n" % formula)
                for i in range(1, tested_faults + 1):
                    fileout.write('%s fault(s)\n' % str(i))
                    faults_combination = 0
                    for j in itertools.combinations(self.processors.dict.keys(), i):

                                # fileout.write('%s \n' % formula)
                        if len(self.get_nulled(variant, j)) >= 2:
                            faults_combination += 1
                            fileout.write('Nulled formula: %s \n' % j)

                    fileout.write(' %s combination failed from %s combinations \n' % (
                    faults_combination, (len(list(itertools.combinations(self.processors.dict.keys(), i))))))
                comb_number += 1

    '''