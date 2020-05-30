class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # if node is none, return none
        if node is None:
            return

        # define next
        next = node.get_next()  # self.next_node

        # if node has prev (True/is not None), set node to next
        if prev:
            node.set_next(prev)  # self.next_node = new_next

        # if next exists, go to next (node=next, prev=node)
        if next:
            self.reverse_list(next, node)

        # change to head if there is no next (tail)
        else:
            self.head = node

