class Interpreter:
    def __init__(self):
        self.stack = []
    
    def PUSH(self, number:int):
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
            instruction , payload = step
            
            if instruction == "PUSH":
                number = numbers[payload]
                self.PUSH(number)
            
            elif instruction == "ADD_TWO_VALUES":
                self.ADD_TWO_VALUES()
            
            elif instruction == "PRINT_ANSWER":
                self.PRINT_ANSWER()

        

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