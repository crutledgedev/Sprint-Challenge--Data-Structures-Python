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
        # Set the stage
        # Reverse Lists must start at head with no previous pointer to None
        previous = None
        current = self.head
        # Your mission: recursive loop until current is = none
        while current is not None:\
                # Loop Logic
            # change next pointer to reverse direction
            next = current.next_node
            current.next_node = previous
            # set previous to current in order to move to the next node
            previous = current
            # set the current pointer to the next node to continue looping to the end of the list
            current = next
        # End Game
        # when current returns None you are at the end of the list and set the new head to previous
        # completing the function and reversing the traversal of the list.
        self.head = previous
