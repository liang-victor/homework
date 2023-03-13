"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

from data_structures.linked_list import ListNode


def add_two_numbers(l1, l2):
    # 2 -> 4 -> 3
    # traverse the linked list, reduce a sum where each element is multiplied by 10**n
    # we need to pass along n in our accumulator
    # 2 + 4*10**1 + 3*10**2...

    value_1 = get_numeric_value(l1)

    value_2 = get_numeric_value(l2)

    return number_to_linked_list(value_1 + value_2)


def get_numeric_value(l):
    running_sum = 0
    n = 0
    while l:
        running_sum += l.val * 10 ** (n)
        l = l.next
        n += 1

    return running_sum


def number_to_linked_list(number):
    # can do this via string manipulation
    # can also do it arithmetically using modulo

    num_str = str(number)

    for i, val in enumerate(int(char) for char in reversed(num_str)):
        if i == 0:
            curr = ListNode(val)
            head = curr
        else:
            next = ListNode(val)
            curr.next = next
            curr = curr.next

    return head
