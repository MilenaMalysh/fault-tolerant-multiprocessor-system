import itertools
from Processors import Processors

__author__ = 'Milena'

from sympy.parsing.sympy_parser import parse_expr

def main():
    faults = {1: '1 fault', 2: '2 faults', 3: '3 faults', 4: '4 faults', 5: '5 faults'}

    processors = Processors()

    for i in range(1,processors.CONST_AMOUNT_PROCESSORS+1):
        print (str(i)+' fault(s)')
        faults_combination = 0
        for j in itertools.combinations(processors.dict.keys(), i):
            processors.generate_combintions(j)
            amount_faults = 0
            with open("formulas.txt", "r") as f:
                for line in f:
                    if not parse_expr(line).subs(processors.dict):
                        amount_faults += 1
            print 'For faults in processors '+str(j)+' there is '+str(amount_faults)+' faults in formulas'
            if not amount_faults ==0:
                faults_combination +=1
        print str(faults_combination)+" combination failed from "+ str(len(list(itertools.combinations(processors.dict.keys(), i))))+' combinations'

if __name__ == "__main__":
    main()
