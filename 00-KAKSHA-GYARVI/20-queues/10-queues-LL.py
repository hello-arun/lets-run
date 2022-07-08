# We aim to implement queues here with the help of linked list
# We Want to implment three functions in the queue
# queue(elemt) => queue the given element to queue
# pop() => pop out the most recent entity and return the same
# isEmpty => return True if queue is empty
# a private varibal to keep track of size


# We need a Node class first of all for a linked list
class Node:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next


class Queue:
    def __init__(self) -> None:
        self.head = Node()
        self.tail = self.head
        self._size = 0  # _means a private varible

    def enqueue(self, val):
        node = Node(val)
        self.tail.next = node
        self.tail = node
        self._size += 1

    def dequeue(self):
        if not self.isEmpty():
            self.head = self.head.next
            self._size -= 1
            return self.head.val
        return

    def isEmpty(self):
        return self._size == 0


if __name__ == "__main__":
    queue = Queue()
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
