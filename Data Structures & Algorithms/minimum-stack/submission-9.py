class MinStack:

    def __init__(self):
        self.stack = []
        self.min_container = []      

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_container:
            if self.min_container[-1] >= val:
                self.min_container.append(val)
        else:
            self.min_container.append(val)

    def pop(self) -> None:
        poped_value = self.stack.pop()
        if self.min_container[-1] == poped_value:
            self.min_container.pop()
            # if self.min_container:
            #     if self.min_container[-1] > self.stack[-1]:
            #         self.min_container.append(self.stack[-1])
            # else:
            #     if self.stack:
            #         self.min_container.append(self.stack[-1])

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        if self.min_container:
            return self.min_container[-1]
        
