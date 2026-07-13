class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)          # add to back

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)          # remove from front

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)           # [1, 2, 3]
print(q.dequeue())  # 1
print(q)            # [2, 3]
print(q.peek())     # 2
print(q.size())     # 2
