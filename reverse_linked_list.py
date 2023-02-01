"""206. Reverse Linked List


"""
from data_structures.linked_list import ListNode


def reverse_list(head):
    p = head
    r = None

    while p is not None:
        if r == None:
            r = ListNode(p.val)
            r.next = None
        else:
            r = ListNode(p.val)
            r.next = last
        last = r
        p = p.next

    return r
