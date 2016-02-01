class Processors:
    CONST_AMOUNT_PROCESSORS = 5;
    def __init__(self):
        self.amount = self.CONST_AMOUNT_PROCESSORS
        self.dict = {}
        for i in range(1, self.CONST_AMOUNT_PROCESSORS + 1):
            self.dict['x'+str(i)] = True

    def display_state(self):
        for i in self.dict:
            print (i,self.dict[i])

    def generate_combintions(self, faults_list):
        self.set_true()
        for i in faults_list:
            self.dict[i] = False

    def set_true(self):
        for i in self.dict:
            self.dict[i] = True


