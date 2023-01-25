"""141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head):
    """Returns true if the linked list has a cycle

    One approach is to hash the nodes as you encounter them and see if you encounter a repeat. However, this uses
    O(n) memory.

    Another approach uses two pointers, fast and slow, that move through the list. If there is a loop, the fast pointer
    can circle around and pass the slow one (i.e. at some point they will coincide at the same node.
    """
    if head is None:
        return False

    # offset the pointers so they don't coincide right at the beginning
    slow = head
    fast = head.next

    while slow is not None and fast is not None and fast.next is not None:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False
