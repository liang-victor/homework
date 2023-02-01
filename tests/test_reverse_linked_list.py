import pytest
from reverse_linked_list import reverse_list
from data_structures.linked_list import LinkedList, ListNode, traverse


def test_simple_list():
    llist = LinkedList([1, 2, 3])

    result = reverse_list(llist.head)
    assert traverse(result) == [3, 2, 1]


def test_empty_list():
    llist = LinkedList([])

    result = reverse_list(llist.head)
    assert result is None
