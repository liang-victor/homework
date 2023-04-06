import pytest
from data_structures.linked_list import LinkedList, ListNode, traverse


def test_insert_value_at_head():
    ll = LinkedList()
    ll.head = ListNode(5)

    ll.insert_value_at_head(2)

    assert traverse(ll) == [2, 5]


def test_insert_value_at_tail():
    ll = LinkedList()
    ll.head = ListNode(5)

    ll.insert_value_at_tail(3)
    assert traverse(ll) == [5, 3]


def test_getitem():
    ll = LinkedList([1, 2, 3])

    assert ll[0].val == 1
    assert ll[1].val == 2
    assert ll[2].val == 3

    with pytest.raises(IndexError):
        ll[3]


def test_delete_node_middle():
    ll = LinkedList([1, 2, 3])

    ll.delete_node(prev_node=ll[0])
    assert traverse(ll) == [1, 3]


def test_remove_matching_values_single_match_at_start():
    ll = LinkedList([1, 2, 3])

    ll.remove_matching_values(1)
    assert traverse(ll) == [2, 3]


def test_remove_matching_values_single_match_in_middle():
    ll = LinkedList([1, 2, 3])

    ll.remove_matching_values(2)
    assert traverse(ll) == [1, 3]


def test_remove_matching_values_single_match_at_end():
    ll = LinkedList([1, 2, 3])

    ll.remove_matching_values(3)
    assert traverse(ll) == [1, 2]


def test_remove_matching_values_multiple_spaced_matches():
    ll = LinkedList([1, 2, 3, 2])

    ll.remove_matching_values(2)
    assert traverse(ll) == [1, 3]


def test_remove_matching_values_multiple_adjacent_matches():
    ll = LinkedList([1, 2, 2, 2, 3])

    ll.remove_matching_values(2)
    assert traverse(ll) == [1, 3]


def test_insert_value_after_first_match():
    ll = LinkedList([1, 2, 3, 4, 5])
    ll.insert_value_after_first_match(55, 3)
    assert traverse(ll) == [1, 2, 3, 55, 4, 5]


def test_reverse():
    ll = LinkedList([1, 2, 3, 4, 5])
    ll.reverse()

    print(ll.head)
    assert traverse(ll) == [5, 4, 3, 2, 1]
