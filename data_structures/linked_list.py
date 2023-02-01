class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

    def __repr__(self):
        return f"ListNode({self.val})"

    def __iter__(self):
        node = self
        while node is not None:
            yield node
            node = node.next


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

    def __repr__(self):
        values = [str(x.val) for x in iter(self)]
        return " -> ".join(values)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node


def traverse(head):
    return [x.val for x in head]
