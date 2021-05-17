class Queue:
    def __init__(self,limit=10):
        self.queue = []
        self.front = None
        self.rear = None
        self.limit = limit
        self.size = 0

    def enqueue(self, data):
        if len(self.queue) >= self.limit:
            print('Queue overflow')
        else:
            self.queue.append(data)
        
        if self.front == None:
            self.front = self.rear = 0  
        else:
            

    def dequeue(self):
        if len(self.queue) <= 0:
            print('Queue underflow')
        else:
            self.queue = self.queue.pop(0)