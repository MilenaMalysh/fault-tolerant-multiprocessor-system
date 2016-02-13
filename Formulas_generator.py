


class Formulas_generator:
    def __init__(self, processors, fault_tolerance, outfile):
        with open(outfile,"w") as f:
            f.write("\n".join(self.generate(len(processors.dict), fault_tolerance, processors.dict)))
        f.close()


    def generate(self, amount_processors, fault_tolerance, processors_dictionary):
        formulas = []
        if fault_tolerance == 1:
            formula = ''
            for i in range(len(processors_dictionary)):
                if (i != len(processors_dictionary) - 1):
                    formula = formula + processors_dictionary.keys()[i] + ' & '
                else:
                    formula = formula + processors_dictionary.keys()[i]
            formulas.append(formula)
            return formulas

        elif fault_tolerance == amount_processors:
            formula = ''
            for i in range(len(processors_dictionary)):
                if (i != len(processors_dictionary) - 1):
                    formula = formula + processors_dictionary.keys()[i] + ' | '
                else:
                    formula = formula + processors_dictionary.keys()[i]
            formulas.append(formula)
            return formulas

        else:
            for j in range(fault_tolerance + 1):
                group1_amount = amount_processors / 2
                group1 = []
                group2 = []
                if (group1_amount >= j) and (amount_processors - group1_amount >= fault_tolerance - j):
                    if (not j == 0):
                        group1 = self.generate(group1_amount, j,
                                               dict(processors_dictionary.items()[len(processors_dictionary) / 2:]))
                    if (not fault_tolerance - j == 0):
                        group2 = self.generate(amount_processors - group1_amount, fault_tolerance - j,
                                               dict(processors_dictionary.items()[:len(processors_dictionary) / 2]))


                if not group1: formulas = formulas + group2
                elif not group2: formulas = formulas + group1
                else:
                    for i in group1:
                        for j in group2:
                            formulas.append(i + " | " + j)
            return formulas






