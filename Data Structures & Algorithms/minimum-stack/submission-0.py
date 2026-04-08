class MinStack:

    def __init__(self):
        self.vals = []
        self.mins = []

    def push(self, val: int) -> None:
        self.vals.append(val)
        if len(self.mins) > 0:
            self.mins.append(min(val, self.mins[-1]))
        else:
            self.mins.append(val)

    def pop(self) -> None:
        if len(self.vals) > 0:
            self.vals.pop()
            self.mins.pop()

    def top(self) -> int:
        if len(self.vals) > 0:
            return self.vals[-1]

    def getMin(self) -> int:
        if len(self.mins) > 0:
            return self.mins[-1]
