"""83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

"""


def delete_duplicates(head):
    current_pointer = head
    new_pointer = None
    last_new_value = None

    while current_pointer:
        if not last_new_value:
            new_pointer = current_pointer
            last_new_value = new_pointer
            new_pointer_head = new_pointer
        elif current_pointer.val != last_new_value.val:
            new_pointer.next = current_pointer
            new_pointer = current_pointer
            last_new_value = new_pointer

        current_pointer = current_pointer.next

    if new_pointer:
        new_pointer.next = None
        return new_pointer_head
    return None
