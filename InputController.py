class InputController:
    def __init__(self):
        self.fault_tolerance = 0
        self.initial_groups = []
        self.blocked_vectors = []
        self.researched_way = False
        self.repeat = False


    def fault_tolerance_request(self):
        while (True):
            fault_tolerance = input('Input fault tolerance of the system')
            if isinstance(fault_tolerance, int):
                self.fault_tolerance = fault_tolerance
                return
            else:
                print('Wrong format. Input number in integer format')

    def initial_groups_request(self):
        while (True):
            initial_groups = input('Input initial groups of processors for generator')
            if isinstance(initial_groups, list) and all(isinstance(item, list) for item in initial_groups):
                self.initial_groups = initial_groups
                return
            else:
                print('Wrong format. Input a list of lists')

    def researched_way_request(self):
        while (True):
            researched_way = raw_input('Do you want to compare results with results of researched method (y/n)')
            if researched_way == 'y':
                self.researched_way = True
                return
            if researched_way == 'n':
                self.researched_way = False
                return
            else:
                print("Wrong format. Input symbol 'y' or 'n'")

    def blocked_vector_request(self):
        while (True):
            blocked_vector = input('Input blocked vector')
            if (isinstance(blocked_vector, list) and len(blocked_vector) == 0) or \
                    (isinstance(blocked_vector, list) and all(isinstance(item, list) for item in blocked_vector)):
                self.blocked_vectors = blocked_vector
                return
            else:
                print('Wrong format. Input a list of lists or empty list')

    def repeat_request(self):
        while (True):
            repeat = raw_input('Do you want to repeat with other values? (y/n)')
            if repeat == 'y':
                self.repeat = True
                return
            if repeat == 'n':
                self.repeat = False
                return
            else:
                print("Wrong format. Input symbol 'y' or 'n'")