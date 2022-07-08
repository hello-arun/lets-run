# We aim to implement stacks here with the help of Array
# We Want to implment three functions in the stack
# push(elemt) => push the given element to stack
# pop() => pop out the most recent entity and return the same
# isEmpty => return True if stack is empty
# a private varibal to keep track of size


# We do need a Node class here
# class Node:
# def __init__(self, val=None, next=None) -> None:
# self.val = val
# self.next = next


class Stack:
    def __init__(self) -> None:
        self._capacity = 100  # Initial Capcaity is 100
        self.head = [0]*self._capacity
        self._size = 0  # _ means a private varible. size 100 seems sufficient
        # Dynamic size can also be implemented but we wont do that here

    def push(self, val):
        if self._size < self._capacity:
            self.head[self._size] = val
            self._size += 1
        else:
            return -1

    def pop(self):
        if not self.isEmpty():
            node = self.head[self._size-1]
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
