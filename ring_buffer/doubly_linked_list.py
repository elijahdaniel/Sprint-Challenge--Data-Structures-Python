"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


my_node = ListNode(12)
my_node.insert_after(25)
my_node.insert_after(100)
my_node.next.insert_after(99)


def iterate_list(node):
    while node is not None:
        print(node.value)
        node = node.next


# iterate_list(my_node)
# my_node = ListNode(12)
# ||
# my_node.next = ListNode(100)
# ||
# ListNode(99)
# ||
# ListNode(25)

# not so efficient: finding a value

# efficient: removing/adding from beginning and end

# delete
# update

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        # tail is the node that points to None (end of list)
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    # Added during stacks and queues GP
    def find_middle(self):
        middle = self.head
        end = self.head

        # look forward two steps
        while end.next != None and end.next.next != None:
            # then take two steps forward
            end = end.next.next
            middle = middle.next

        return middle

    # head should now be tail
    # tail should now be head
    # no recursion, no other data structures
    def reverse_list(self):
        pass

    def iterate_nodes(self):
        total = 0
        node = self.head
        while node is not None:
            total += 1
            node = node.next

        return total

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # wrap the given value in a ListNode
        new_node = ListNode(value, None, None)
        self.length += 1

        # handle if list has a head
        if self.head:
            # point new node with next to the old head
            new_node.next = self.head
            # points old head with prev the new node
            self.head.prev = new_node
            # reset self.head to new node
            # tells link list, this is the new head
            self.head = new_node

        # handle if list has no head
        else:
            # set empty self.head + self.tail (no head/no tail) to new_node
            self.head = new_node
            self.tail = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        value = self.head.value

        self.delete(self.head)

        # Returns the value of the removed Node.
        return value

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # create new node
        new_node = ListNode(value)  # default, none, none after value

        # adding to length
        self.length += 1

        # there is a tail - have something
        if self.tail:
            # pointing old node with next to new node
            self.tail.next = new_node
            # points nodes previous to current tail
            new_node.prev = self.tail
            # tells self.tail in linked list that self.tail is the new_node
            # self.tail = new_node

        # there is no tail - have nothing
        else:
            # set empty self.tail + self.head (no tail/no head) to new_node
            # self.tail = new_node
            self.head = new_node

        # brought outside of 'if' for dryer code
        self.tail = new_node

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        # can be solved with:
        # value = self.tail.value
        # self.delete(self.tail)

        # written out the long way:

        # save the tail's value
        value = self.tail.value

        # if 0 nodes
        if not self.tail:
            return

        # if head and tail are the same (1 node)
        elif self.head == self.tail:
            # set them to none since we're removing them
            self.head = None
            self.tail = None

        # if more than 1 node
        else:

            # update self.tail to refer to the node in front of it
            self.tail = self.tail.prev
            # tail's next is None since it is now the tail
            self.tail.next = None

        self.length -= 1

        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        # save the node's value as value
        value = node.value
        # delete the node with the .delete method
        self.delete(node)
        # call add_to_head with the saved value
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        # save the value
        value = node.value
        # delete the node
        self.delete(node)
        # call add_to_tail with value
        self.add_to_tail(value)

    # delete
    # add_to_tail

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):

        # if list is empty
        if not self.head:
            print("List is empty")
            return

        # subtract from the list's length (moved to after checking if list is empty)
        self.length -= 1

        # if list only has one item
        if self.head == self.tail:
            # delete from list / make empty (set to none)
            self.head = None
            self.tail = None

        # if we have a least two nodes, and the node we want to delete is the head
        if node == self.head:
            # assign self.head = node.next (the node after (next))
            self.head = node.next
            # set self.head.prev to none
            self.head.prev = None

        # if we have a least two nodes, and the node we want to delete is the tail
        if node == self.tail:
            # reroute self.tail to the node's previous
            # rerouting tail to be the previous value
            self.tail = node.prev
            # set tail next to None since new tail is the new tail
            self.tail.next = None
        else:
            # route around to delete method above
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        # walk through the entire list
        # keep track of the biggest value we've found

        highest_value = self.head.value
        current_node = self.head

        while current_node is not None:
            # check the value of current node
            if current_node.value > highest_value:
                highest_value = current_node.value

            # bump along to next node
            current_node = current_node.next

        return highest_value


# dll = DoublyLinkedList()
# dll.add_to_tail(1)
# dll.add_to_tail(2)
# dll.add_to_tail(3)
# dll.add_to_tail(4)
# dll.add_to_tail(5)

# middle = dll.find_middle()
# print(middle.value)
