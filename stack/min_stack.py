class MinStack:
    # basically a priority queue with stack

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # all the tricks here
        # determine new min value
        if not self.stack:
            current_min = val
        else:
            current_min = min(val, self.stack[-1][1])

        # store the current value and min value together!
        self.stack.append((val, current_min)) 

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
