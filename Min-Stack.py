class MinStack:

    def __init__(self):
        self.items= []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        self.items.append(val)
        if not self.min_stack  or val <= self.min_stack[-1]:
            self.min_stack.append(val)
            
    def pop(self) -> None:
        if self.items:
            val = self.items.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
        
    def top(self) -> int:
        if self.items:
            return self.items[-1]
        
    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()