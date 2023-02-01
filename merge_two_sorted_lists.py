"""21. Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
from data_structures.linked_list import ListNode


def merge_two_lists(list1, list2):
    """
    1         5          8         15
      3   4         7        12
    """

    p = list1
    q = list2

    if p is None:
        return q
    if q is None:
        return p

    # find initial pointer s for sorted list
    if p.val <= q.val:
        s = p
        p = p.next
    else:
        s = q
        q = q.next

    head = s

    # splice lists together until one list runs out
    while p is not None and q is not None:
        if p.val <= q.val:
            s.next = p
            s = p
            p = p.next
        else:
            s.next = q
            s = q
            q = q.next

    # attach remainder of either list to the end
    if p is not None:
        s.next = p

    if q is not None:
        s.next = q

    return head
