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

    def __getitem__(self, index):
        for i, node in enumerate(self):
            if i == index:
                return node
        raise IndexError

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def insert_value_at_head(self, value):
        node = ListNode(value)
        node.next = self.head
        self.head = node

    def insert_value_at_tail(self, value):
        end_node = ListNode(value)
        for node in self:
            pass
        node.next = end_node

    def delete_node(self, prev_node=None):
        """This is a bit clunky"""
        if not prev_node:
            self.head = self.head.next
            return

        if prev_node.next and prev_node.next.next:
            prev_node.next = prev_node.next.next
            return

        else:
            prev_node.next = None

    def remove_matching_values(self, x):
        prev_node = None
        for node in self:
            if node.val == x:
                self.delete_node(prev_node)
            else:
                prev_node = node

    def insert_value_after_first_match(self, value, x):
        new_node = ListNode(value)
        for node in self:
            if node.val == x:
                next_node = node.next
                node.next = new_node
                new_node.next = next_node
                break

    def reverse(self):
        node = self.head
        prev = None

        while node:
            next_node = node.next
            node.next = prev

            prev = node
            node = next_node
        self.head = prev


def traverse(head):
    return [x.val for x in head]
