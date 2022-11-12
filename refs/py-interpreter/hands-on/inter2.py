class Interpreter:
    def __init__(self):
        self.stack = []
        self.environment = {}
    
    def STORE_NAME(self, name):
        val = self.stack.pop()
        self.environment[name] = val
    
    def LOAD_NAME(self, name):
        val = self.environment[name]
        self.stack.append(val)
    
    def parse_argument(self, instruction, argument, what_to_execute):
        numbers = ["LOAD_VALUE"]
        names = ["LOAD_NAME", "STORE_NAME"]
        
        if instruction in numbers:
            argument = what_to_execute["numbers"][argument]
        elif instruction in names:
            argument = what_to_execute["names"][argument]
        
        return argument

    def LOAD_VALUE(self, number:int):
        self.stack.append(number)
    
    def ADD_TWO_VALUES(self):
        first = self.stack.pop()
        second = self.stack.pop()
        total = first + second
        self.stack.append(total)

    def PRINT_ANSWER(self):
        answer = self.stack.pop()
        print(answer)
    
    def run_code(self,code):
        steps = code["steps"]
        numbers = code["numbers"]

        for step in steps:
            instruction , argument = step
            
            if instruction == "LOAD_VALUE":
                self.LOAD_VALUE(argument)            
            
            elif instruction == "ADD_TWO_VALUES":
                self.ADD_TWO_VALUES()
            
            elif instruction == "PRINT_ANSWER":
                self.PRINT_ANSWER()

            elif instruction == "STORE_NAME":
                self.STORE_NAME(argument)
            
            elif instruction == "LOAD_NAME":
                self.LOAD_NAME(argument)



what_to_execute = {
    "steps": [("PUSH", 0),  # the first number
                     ("PUSH", 1),  # the second number
                     ("ADD_TWO_VALUES", None),
                     ("PUSH", 2),
                     ("ADD_TWO_VALUES", None),
                     ("PRINT_ANSWER", None)],
    "numbers": [7, 5, 3] 
}

inter = Interpreter()
inter.run_code(what_to_execute)