class MinStack:

    def __init__(self):
        self.elements = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.elements.append(val)
        if not self.min_stack or self.min_stack[-1] > val:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.min_stack.pop()
        return self.elements.pop()

    def top(self) -> int:
        return self.elements[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
