from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        # declare initial limit
        self.capacity = capacity
        # declare current item
        self.current = 0
        # declare storage type of doubly linked list
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if capacity exists add item
        if len(self.storage) < self.capacity:
            self.storage.add_to_head(item)
            # if item is first item, set to head
            if len(self.storage) == 1:
                self.current = self.storage.head
            return
        # if capacity is full
        elif len(self.storage) == self.capacity:
            # set node value
            self.current.value = item
            # check for previous node
            if self.current.prev is not None:
                # move pointer
                self.current = self.current.prev
            else:
                # set end node to tail
                self.current = self.storage.tail

    def get(self):
        # create a list to hold the returned values/buffer
        buffer_contains = []
        # start at tail
        current = self.storage.tail
        # create a for in loop over length of storage
        for x in range(len(self.storage)):
            # append current value
            buffer_contains.append(current.value)
            # set current pointer to previous
            current = current.prev
        # return the buffer list
        return buffer_contains
