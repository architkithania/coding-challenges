from LinkedList import LinkedLists
from LinkedList import Node

def find_intersection(list1, list2):
    head = join(list1, list2)
    current = head
    while current.next is not None:
        last = current
        current = current.next
        last.next = None
    return current.val

def join(list1, list2):
    current = list1
    while current.next is not None:
        current = current.next
    current.next = list2
    return list1

n6 = Node(val=10)
n5 = Node(val=8, next_val=n6)
n4 = Node(val=7, next_val=n5)
head1 = Node(val=3, next_val=n4)
n2 = Node(val=1, next_val=n5)
head2 = Node(99, next_val=n2)
