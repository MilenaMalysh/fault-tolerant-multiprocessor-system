from Processors import Processors
from PrTester import PrTester
from Formulas_generator import *
import sys

__author__ = 'Milena'

def main():
    amount_processor = 8;
    fault_tolerance = 4;
    formulas_file = sys.argv[1]


    processors = Processors(amount_processor)
    generator = Formulas_generator(processors, fault_tolerance, formulas_file)
    tester = PrTester(formulas_file, processors,fault_tolerance+2)


if __name__ == "__main__":
    main()
