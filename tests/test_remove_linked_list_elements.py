import pytest
from remove_linked_list_elements import remove_elements
from data_structures.linked_list import ListNode, LinkedList, traverse


def test_remove_middle_element():
    llist = LinkedList([1, 2, 3, 4, 5])
    val = 3
    result = remove_elements(llist.head, val)

    assert traverse(result) == [1, 2, 4, 5]


def test_remove_first_element():
    llist = LinkedList([1, 2, 3, 4, 5])
    val = 1
    result = remove_elements(llist.head, val)

    assert traverse(result) == [2, 3, 4, 5]


def test_remove_last_element():
    llist = LinkedList([1, 2, 3, 4, 5])
    val = 5
    result = remove_elements(llist.head, val)

    assert traverse(result) == [1, 2, 3, 4]


def test_remove_repeated_element():
    llist = LinkedList([1, 2, 3, 4, 5, 3])
    val = 3
    result = remove_elements(llist.head, val)

    assert traverse(result) == [1, 2, 4, 5]


def test_no_match():
    llist = LinkedList([1, 2, 3, 4, 5])
    val = 7
    result = remove_elements(llist.head, val)

    assert traverse(result) == [1, 2, 3, 4, 5]


def test_all_match():
    llist = LinkedList([7, 7, 7, 7])
    val = 7
    result = remove_elements(llist.head, val)

    assert result is None
