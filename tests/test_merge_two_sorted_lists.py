import pytest
from merge_two_sorted_lists import merge_two_lists
from data_structures.linked_list import ListNode, LinkedList, traverse


def test_merge_two_lists():
    list1 = LinkedList([1, 2, 4])
    list2 = LinkedList([3])

    result = merge_two_lists(list1.head, list2.head)
    expected = [1, 2, 3, 4]

    assert traverse(result) == expected


def test_duplicate_middle_value():
    list1 = LinkedList([1, 2, 4])
    list2 = LinkedList([2, 3])

    result = merge_two_lists(list1.head, list2.head)
    expected = [1, 2, 2, 3, 4]

    assert traverse(result) == expected


def test_duplicate_starting_value():
    list1 = LinkedList([1, 2, 4])
    list2 = LinkedList([1, 3])

    result = merge_two_lists(list1.head, list2.head)
    expected = [1, 1, 2, 3, 4]

    assert traverse(result) == expected


def test_duplicate_ending_value():
    list1 = LinkedList([1, 2, 4])
    list2 = LinkedList([3, 4])

    result = merge_two_lists(list1.head, list2.head)
    expected = [1, 2, 3, 4, 4]

    assert traverse(result) == expected


def test_both_empty():
    list1 = LinkedList([])
    list2 = LinkedList([])

    result = merge_two_lists(list1.head, list2.head)
    expected = []

    assert result is None
