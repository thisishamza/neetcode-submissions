class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack)==0 or self.stack[-1][1] == val:
            self.stack.append((val, val))
        elif self.stack[-1][1] > val:
            self.stack.append((val, val))
        elif self.stack[-1][1] < val:
            self.stack.append((val, self.stack[-1][1]))

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()


    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack)>0:
            return self.stack[-1][1]
        
