class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.topStack = 0
        self.size = 0
        

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.topStack = x
        self.size += 1

    def pop(self) -> int:
        x = 0
        while self.q1:
            if len(self.q1) == 1:
                x = self.q1.popleft()
            else:
                self.q2.append(self.q1.popleft())
        while self.q2:
            self.q1.append(self.q2.popleft())
        if len(self.q1) > 0 :
            self.topStack = self.q1[-1]
        elif len(self.q1) == 0 :
            self.topStack = None
        
        self.size -= 1
        return  x
        


    def top(self) -> int:
        return self.topStack

    def empty(self) -> bool:
        return self.size == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()