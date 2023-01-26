class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

    def __repr__(self):
        return self.val


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        if values is not None:
            for i, value in enumerate(values):
                if i == 0:
                    node = ListNode(value)
                    self.head = node
                else:
                    node.next = ListNode(value)
                    node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node
