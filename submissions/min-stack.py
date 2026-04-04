# Problem #155: Min Stack
# Difficulty : Medium
# Language   : python3
# Runtime    : 12 ms
# Memory     : 21.4 MB
# URL        : https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        if len(self.min) == 0:
            self.min.append(val)
        else:
            self.min.append(min(self.min[-1], val))
        self.stack.append(val)

    def pop(self) -> None:
        self.min = self.min[:-1]
        self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()