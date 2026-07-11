class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        temp = []
        mini = self.stack[-1]

        while len(self.stack):
            mini = min(mini, self.stack[-1])
            val = self.stack.pop()
            temp.append(val)

        
        while len(temp):
            val = temp.pop()

            self.stack.append(val)
        
        return mini
