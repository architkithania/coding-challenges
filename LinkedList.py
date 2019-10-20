class Node:
    def __init__(self, val=None, next_val=None):
        self.val = val
        self.next = next_val

class LinkedLists:
    def __init__(self, head=None, init_list=[]):
        self.head = head
        if len(init_list) > 0:
            for item in init_list:
                self.append(item)

    def __repr__(self):
        string = "["
        current = self.head
        while current is not None:
            string += str(current.val)
            if current.next is not None:
                string += ","
            current = current.next

        string += "]"
        return string
    
    def append(self, data):
        if self.head == None:
            self.head = Node(data)
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data)

    def prepend(self, data):
        if self.head is not None:
            new_head = Node(data)
            new_head.next = self.head
            self.head = new_head
        else:
            self.head = Node(data)
    
    def remove_by_value(self, data):
        if self.head is not None:
            current = self.head
            while current.next is not None:
                if current.next.val == data:
                    if current.next.next != None:
                        current.next = current.next.next
                        break
                    else:
                        current.next = None
                        break
                current = current.next

    def join(self, linked_list):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = linked_list
