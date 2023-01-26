import pytest
from remove_duplicates_from_sorted_list import delete_duplicates
from data_structures.linked_list import LinkedList, ListNode, traverse


def test_remove_from_start():
    llist = LinkedList([1, 1, 2])
    result = delete_duplicates(llist.head)

    assert traverse(result) == [1, 2]


def test_remove_from_end():
    llist = LinkedList([1, 2, 2])
    result = delete_duplicates(llist.head)

    assert traverse(result) == [1, 2]


def test_remove_from_middle():
    llist = LinkedList([1, 2, 2, 3])
    result = delete_duplicates(llist.head)

    assert traverse(result) == [1, 2, 3]
