class CalculatorError(Exception): pass
class InvalidInputError(CalculatorError): pass
class StringInputError(CalculatorError): pass

class Calculator:

    def __init__(self, val=0.00):
        self.acc = val
    
    def set_accumulator(self, a):
        self.acc = a
    
    def get_accumulator(self):
        return self.acc
    
    def add(self, x):
        if isinstance(x, str) :
            raise StringInputError()
        self.acc += x
        return self.acc
    
    def subtract(self, x):
        if isinstance(x, str) :
            raise StringInputError()
        self.acc -= x
        return self.acc

    def multiply(self, x):
        if isinstance(x, str) :
            raise StringInputError()
        self.acc = self.acc * x
        return self.acc
    
    def divide(self, x):
        if isinstance(x, str) :
            raise StringInputError()
        if x == 0:
            raise InvalidInputError('Error')  
        self.acc = self.acc / x
        return self.acc

    def get_status(self):
        return "Result: " + str(self.acc)