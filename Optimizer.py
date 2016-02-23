import itertools
from sympy.simplify.cse_main import cse
from sympy.parsing.sympy_parser import parse_expr


class Optimizer:
    def __init__(self, filein, file_agg, fileout):
        with open(filein) as f:
            self.filein_arr = f.readlines()
        self.fileagg = file_agg
        self.fileout = fileout
        self.optimize()


    def optimize(self):
        fi = open(self.fileagg, "w+")

        for i in range(2, len(self.filein_arr)):
            for j in itertools.combinations(self.filein_arr, i):
                considered_formulas = self.find_formulas(j)
                self.check_matches(considered_formulas)

        """for i1 in range(len(self.filein_arr)-1):
            for i2 in range(len(self.filein_arr)-1):
                if (i2>i1):
                    if cse([parse_expr(self.filein_arr[i1]), parse_expr(self.filein_arr[i2])],optimizations='basic')[0]:
                        fi.write(self.filein_arr[i1].rstrip()+' | '+self.filein_arr[i2].rstrip()+"\n")"""
        fi.close()

    def find_formulas(self, formulas_list):
        formul_list = []
        for i in self.filein_arr:
            if i in formulas_list:
                formul_list.append(i)
        return formul_list
    # TODO: add check_matches method

    """def check_matches(self, considered_formulas):
        for i in considered_formulas:
            for k in range (len(parse_expr(i).args))
            for j in itertools.combinations(parse_expr(i).args, i):"""
