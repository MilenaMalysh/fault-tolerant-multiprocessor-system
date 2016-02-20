from collections import OrderedDict


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
                group2_amount = amount_processors - group1_amount
                group1 = []
                group2 = []
                processors_group = self.divide_processors([group1_amount, group2_amount], processors_dictionary)
                if (group2_amount >= j) and (group1_amount >= fault_tolerance - j):
                    if (not fault_tolerance - j == 0):
                        group1 = self.generate(group1_amount, fault_tolerance - j,processors_group.get(1))
                    if (not j == 0):
                        group2 = self.generate(group2_amount, j, processors_group.get(2))


                if not group1: formulas = formulas + group2
                elif not group2: formulas = formulas + group1
                else:
                    for i in group1:
                        for k in group2:
                            formulas.append(i + " | " + k)
            return formulas


    def divide_processors(self, amounts, processors_dictionary):
        divided_processors ={}
        j = 0
        for i in amounts:
            j+=1
            #divided_processors.update({j:dict(processors_dictionary.items()[:i])})
            #processors_dictionary = dict(processors_dictionary.items()[i:])

            divided_processors.update({j:OrderedDict(processors_dictionary.items()[:i])})
            processors_dictionary = OrderedDict(processors_dictionary.items()[i:])

        return divided_processors






