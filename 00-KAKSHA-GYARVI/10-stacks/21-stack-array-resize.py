# We aim to implement stacks here with the help of Array
# We Want to implment three functions in the stack
# push(elemt) => push the given element to stack
# pop() => pop out the most recent entity and return the same
# isEmpty => return True if stack is empty
# a private varibal to keep track of size

# For resizing array
# ・push(): double size of array s[] when array is full.
# ・pop(): halve size of array s[] when array is one-quarter full.


class Stack:
    def __init__(self) -> None:
        self._capacity = 2  # Initial Capcaity is 100
        self.head = [0]*self._capacity
        self._size = 0  # _ means a private varible. size 100 seems sufficient

    def push(self, val):
        if self._size==self._capacity:
            self.resize(2*self._capacity)
        self.head[self._size] = val
        self._size += 1

    def pop(self):
        if not self.isEmpty():
            if self._size == self._capacity//4:
                self.resize(self._capacity//2)
            node = self.head[self._size-1]
            self._size -= 1
            return node
        return

    def isEmpty(self):
        return self._size == 0

    def resize(self, capacity:int):
        self._capacity=capacity
        stack=[0]*capacity
        for i in range(self._size):
            stack[i] = self.head[i]
        self.head = stack

if __name__ == "__main__":
    stack=Stack()
    for i in range(1,10):
        stack.push(i)
        print(f"{i} added, stack capacity: {stack._capacity}")
    for i in range(1,11):
        print(f"{stack.pop()} pop, stack capacity: {stack._capacity}")
