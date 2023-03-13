import pytest
from add_two_numbers import get_numeric_value, add_two_numbers, number_to_linked_list
from data_structures.linked_list import LinkedList


def linked_list_to_list(head):
    curr = head
    result = []

    while curr != None:
        result.append(curr.val)
        curr = curr.next
    return result


def test_get_numeric_value():
    linked_list = LinkedList(values=[2, 4, 3]).head

    number = get_numeric_value(linked_list)
    assert number == 342


def test_number_to_linked_list():
    number = 807
    expected = [node.val for node in LinkedList(values=[7, 0, 8])]

    resulting_linked_list_head = number_to_linked_list(number)
    result = linked_list_to_list(resulting_linked_list_head)

    assert result == expected


def test_add_two_numbers_example_1():
    l1 = LinkedList(values=[2, 4, 3]).head
    l2 = LinkedList(values=[5, 6, 4]).head

    result_head = add_two_numbers(l1, l2)

    result = linked_list_to_list(result_head)
    assert result == [7, 0, 8]


def test_add_two_numbers_example_2_all_zeros():
    l1 = LinkedList(values=[0]).head
    l2 = LinkedList(values=[0]).head

    result_head = add_two_numbers(l1, l2)

    result = linked_list_to_list(result_head)
    assert result == [0]


def test_add_two_numbers_example_3_all_nines():
    l1 = LinkedList(values=[9, 9, 9, 9, 9, 9, 9]).head
    l2 = LinkedList(values=[9, 9, 9, 9]).head

    result_head = add_two_numbers(l1, l2)

    result = linked_list_to_list(result_head)
    assert result == [8, 9, 9, 9, 0, 0, 0, 1]
