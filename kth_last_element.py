from LinkedList import LinkedLists

def kth_last(head, k):
    current = head
    while True:
        test = current
        for i in range(k - 1):
            test = test.next
        if test.next is None:
            return current.val
        current = current.next;


