class Stack:
    def __init__(self, limit = 10):
        self.limit = limit
        self.stack = []

    def push(self, data):
        if len(self.stack)>=self.limit:
            print('stack overflow!')
        else:
            self.stack.append(data)
    def pop(self, data):
        if len(self.stack)<=0:
            print('stack underflow!')
        else:            
            self.stack.pop()
    def peek(self):
        if len(self.stack)<=0:
            print('stack underflow!')
        else:            
            self.stack[-1]

s = Stack(limit=5)
[s.push(i) for i in range(1,7)]
print(s.stack)