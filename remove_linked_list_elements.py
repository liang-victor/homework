"""208. Remove linked list elements

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

"""


def remove_elements(head, val):
    p = head
    r = None

    while p is not None:
        if p.val != val:
            if not r:
                r = p
                new_head = r
            else:
                r.next = p
                r = p
        p = p.next
    if not r:
        return None

    r.next = None
    return new_head
