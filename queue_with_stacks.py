class Stack:
    def __init__(self):
        self.__elements = []

    def push(self, element):
        self.__elements.append(element)

    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            return None

    def top(self):
        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return None


class Queue:
    def __init__(self):
        self.__elements = Stack()

    def enqueue(self, element):
        self.__elements.push(element)

    def dequeue(self):
        temp_stack = Stack()
        while self.__elements.top() is not None:
            temp_stack.push(self.__elements.pop())
        top = temp_stack.pop()
        while temp_stack.top() is not None:
            self.__elements.push(temp_stack.pop())
        return top
