import pytest
from linked_list_cycle import ListNode, has_cycle


def test_example_1():
    a = ListNode(3)
    b = ListNode(2)
    c = ListNode(0)
    d = ListNode(-4)

    a.next = b
    b.next = c
    c.next = d
    d.next = b

    assert has_cycle(a) == True


def test_no_cycle():
    a = ListNode(3)
    b = ListNode(2)
    c = ListNode(0)
    d = ListNode(-4)

    a.next = b
    b.next = c
    c.next = d

    assert has_cycle(a) == False


def test_example_2():
    a = ListNode(1)
    b = ListNode(2)

    a.next = b
    b.next = a

    assert has_cycle(a) == True


def test_example_3():
    a = ListNode(1)

    assert has_cycle(a) == False
