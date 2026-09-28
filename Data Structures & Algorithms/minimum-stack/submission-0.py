class MinStack:

    def __init__(self):
        self.s = []
        self.order = []

    def push(self, val: int) -> None:
        self.s.append(val)
        minimum = min(val, self.order[-1] if self.order else val)
        self.order.append(minimum)

    def pop(self) -> None:
        self.s.pop()
        self.order.pop()     

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.order[-1]
