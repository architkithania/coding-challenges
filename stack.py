'''
Implement a stack which performs pop, push, max in constant time
'''


class Stack:
    def __init__(self):
        self.__items = []
        self.max = None

    def pop(self):
        if len(self.__items) == 0:
            raise Exception("Stack Underflow")
        return self.__items.pop()

    def push(self, item):
        self.__items.append(item)
        if self.max is None:
            self.max = item
        else:
            self.max = max(self.max, item)


stack = Stack()
stack.push(3)
stack.push(1)
stack.push(2)
print(stack.pop())
print(stack.pop())
print(stack.max)
