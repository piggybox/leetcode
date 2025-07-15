\
from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        # Push element onto the stack
        self.queue.append(x)

        # Rotate the queue to make the last pushed element the first one!
        for _ in range(len(self.queue) - 1): # n-1 rotations
            self.queue.append(self.queue.popleft())
        

    def pop(self) -> int:
        # Pop the top element from the stack
        return self.queue.popleft()
        

    def top(self) -> int:
        # Get the top element of the stack
        return self.queue[0]
        

    def empty(self) -> bool:
        # Check if the stack is empty
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()