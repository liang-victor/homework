"""232. Implement Queue using Stacks

https://leetcode.com/problems/implement-queue-using-stacks/


"""


class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        """We do copy reversed input to output but then it's O(1) to pop values after"""
        self.populate_output_if_needed()
        return self.output.pop()

    def peek(self) -> int:
        self.populate_output_if_needed()
        return self.output[-1]

    def empty(self) -> bool:
        return not (self.input or self.output)

    def populate_output_if_needed(self):
        if not self.output:
            self.output = self.input[::-1]
            self.input.clear()
