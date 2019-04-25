class StackError(Exception): pass
class OutOfRangeError(StackError): pass

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,val):
        self.stack.append(val)


    def pop(self):
        if len(self.stack) <= 0:
            raise OutOfRangeError()
        else:
            return self.stack.pop()
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    def size(self):
        return len(self.stack)

    def peek(self):
        if len(self.stack) <= 0:
            raise OutOfRangeError()
        else:
            return self.stack[-1]