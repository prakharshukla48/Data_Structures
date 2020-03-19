class Queue:
    def __init__(self, n):
        self.max_n = n
        self.queue = []
        self.front = -1
        self.rear = -1

    def enqueue(self, x):
        if (self.rear >= self.max_n):
            return -1

        self.queue.append(x)
        if (self.front == self.rear == -1):
            self.front = self.front + 1
            self.rear = self.rear + 1
        else:
            self.rear = self.rear + 1

    def dequeue(self):
        if (self.front == self.rear == -1):
            return -1

        if (self.front > self.rear):
            return -1
        self.front = self.front + 1
        self.queue.pop(0)

    def display(self):
        print (self.queue)

if __name__ == '__main__':
    q = Queue(5)
    for i in range(5):
        q.enqueue(i)
        q.display()

    for j in range(5):
        q.dequeue()
        q.display()
    
    
