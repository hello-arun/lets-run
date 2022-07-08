# We aim to implement queues here with the help of Array of fixed capacity
# We Want to implment three functions in the queue
# queue(elemt) => queue the given element to queue
# pop() => pop out the most recent entity and return the same
# isEmpty => return True if queue is empty
# a private varibal to keep track of size


class Queue:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.q = [0]*capacity
        self.head = 0
        self.tail = 0
        self._size = 0  # _means a private varible

    def enqueue(self, val):
        if self._size != self.capacity:
            self.q[self.tail] = val
            self.tail = (self.tail+1) % self.capacity
            self._size += 1

    def dequeue(self):
        if not self.isEmpty():
            val = self.q[self.head]
            self.head = (self.head+1) % self.capacity
            self._size -= 1
            return val
        return

    def isEmpty(self):
        return self._size == 0


if __name__ == "__main__":
    queue = Queue(15)
    for i in range(5):
        queue.enqueue(i)
        print(f"Queued:   {i}")
    for i in range(3):
        print(f"Dequeued: {queue.dequeue()}")
    for i in range(12, 16):
        queue.enqueue(i)
        print(f"Queued:   {i}")
    for i in range(5):
        print(f"Dequeued: {queue.dequeue()}")
