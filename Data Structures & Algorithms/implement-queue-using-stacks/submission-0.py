class MyQueue:

    def __init__(self):
        self.inputs = []
        self.outputs = []

    def push(self, x: int) -> None:
        self.inputs.append(x)

    def pop(self) -> int:
        if not self.outputs:
            while self.inputs:
                self.outputs.append(self.inputs.pop())
        return self.outputs.pop()

    def peek(self) -> int:
        if not self.outputs:
            while self.inputs:
                self.outputs.append(self.inputs.pop())
        return self.outputs[-1]

    def empty(self) -> bool:
        return not self.inputs and not self.outputs


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()