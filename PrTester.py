import itertools
from sympy.parsing.sympy_parser import parse_expr



class PrTester:
    def __init__(self, filein, processors, tested_faults):
        self.filein = filein
        self.processors = processors
        self.tested_faults = tested_faults
        self.test()

    def test(self):
        for i in range(1,self.tested_faults+1):
            print (str(i)+' fault(s)')
            faults_combination = 0
            for j in itertools.combinations(self.processors.dict.keys(), i):
                self.processors.generate_combintions(j)
                amount_faults = 0
#                with filein as f:
                with open(self.filein) as filein:
                    for line in filein:
                        if not parse_expr(line).subs(self.processors.dict):
                            amount_faults += 1
                            print line
                print 'For faults in processors '+str(j)+' there is '+str(amount_faults)+' faults in formulas'
                if not amount_faults ==0:
                    faults_combination +=1
            print str(faults_combination)+" combination failed from "+ str(len(list(itertools.combinations(self.processors.dict.keys(), i))))+' combinations'


