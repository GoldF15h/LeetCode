class MyStack:

    def __init__(self):
        self.queue = []
        

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if len(self.queue) :
            op = self.queue[-1]
            self.queue.pop()
            return op
        return
        

    def top(self) -> int:
        if len(self.queue) :
            return self.queue[-1]
        return
        

    def empty(self) -> bool:
        if len(self.queue) :
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()