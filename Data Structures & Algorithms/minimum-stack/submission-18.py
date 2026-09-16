import heapq

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.running_min = float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.running_min:
            self.min_stack.append(val)
            self.running_min = val

    def pop(self) -> None:
        to_return = self.stack.pop()
        if to_return == self.min_stack[-1]:
            self.min_stack.pop()
            if self.min_stack != []:
                self.running_min = self.min_stack[-1]
            else:
                self.running_min = float('inf')
            
        
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
