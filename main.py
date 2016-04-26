from Optimizer import Optimizer
from Processors import Processors
from PrTester import PrTester
from Formulas_generator import *
from sympy.simplify.cse_main import cse
import sys

__author__ = 'Milena'

def main():
    amount_processor = 7
    fault_tolerance = 3
    formulas_file = sys.argv[1]
    agglutinated_file = sys.argv[2]
    optimized_file = sys.argv[3]


    processors = Processors(amount_processor)
    generator = Formulas_generator(processors, fault_tolerance, formulas_file)
    optimizer = Optimizer(generator.origin_formulas_arr, amount_processor, fault_tolerance, processors, optimized_file)
    optimizer.optimize()
    tester = PrTester(formulas_file, processors,fault_tolerance+3)



    #from sympy.abc import a, b, c, d, e, f, g ,h ,i, j, k, l, m, n
    #cse([(f & g | a & b | d & e),(a & b & c | f & e | f & g | d & e)], optimizations='basic')
    #cse([(y & x ),(x & y | z)])[0][0][1]


    #((a & b | f | g & e).has(a & b | l & e))  !!!!
    #simplify_logic(f & g | l & e | d & e |a & b & c | f & e | l & e, True) !!!!


if __name__ == "__main__":
    main()
