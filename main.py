from Optimizer import Optimizer
from Processors import Processors
from PrTester import PrTester
from Formulas_generator import *
from sympy.simplify.cse_main import cse
import sys

__author__ = 'Milena'

def main():
    amount_processor = 7;
    fault_tolerance = 3;
    formulas_file = sys.argv[1]
    agglutinated_file = sys.argv[2]
    optimized_file = sys.argv[3]


    processors = Processors(amount_processor)
    generator = Formulas_generator(processors, fault_tolerance, formulas_file)
    optimizer = Optimizer(formulas_file, agglutinated_file, optimized_file)
    tester = PrTester(formulas_file, processors,fault_tolerance+2)


    #cse([(y & x ),(x & y | z)])[0][0][1]
    #((a & b | f | g & e).has(a & b | g & e))


if __name__ == "__main__":
    main()
