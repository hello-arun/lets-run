# We aim to implement stacks here with the help of linked list
# We Want to implment three functions in the stack
# push(elemt) => push the given element to stack
# pop() => pop out the most recent entity and return the same
# isEmpty => return True if stack is empty
# a private varibal to keep track of size


# We need a Node class first of all for a linked list
class Node:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next


class Stack:
    def __init__(self) -> None:
        self.head = Node()
        self._size = 0  # _means a private varible

    def push(self, val):
        node = Node(val, self.head)
        self.head = node
        self._size += 1

    def pop(self):
        if not self.isEmpty():
            node = self.head.val
            self.head = self.head.next
            self._size -= 1
            return node
        return

    def isEmpty(self):
        return self._size == 0


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    print(stack.pop())
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.pop())
    stack.push(4)
    print(stack.pop())
    print(stack.pop())
