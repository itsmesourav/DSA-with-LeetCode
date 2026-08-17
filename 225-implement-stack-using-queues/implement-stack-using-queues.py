from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        # Put new element into the empty queue
        self.q2.append(x)

        # Move all existing elements behind it
        while self.q1:
            self.q2.append(self.q1.popleft())

        # Swap the queues
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1