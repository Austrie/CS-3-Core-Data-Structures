#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
        return self.list.length()

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Insert given item
        return self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        if self.is_empty():
            return None
        else:
            return self.list.head.data

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return front item, if any
        if self.is_empty():
            raise ValueError("Queue is empty!")

        head = self.list.head.data
        self.list.delete(head)
        return head


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        self.front_position = None
        self.size = 0
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)
        else:
            for i in range(10):
                self.enqueue(None)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty
        return True if self.size is 0 else False

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
        return self.size

    ''' This function is amortized O(1) '''
    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Insert given item
        if self.is_empty():
            self.front_position = 0
        self.list[self.length()] = item
        if item is not None:
            self.size += 1

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        if self.is_empty():
            return None
        return self.list[self.front_position]

    ''' This function is amortized O(1) '''
    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return front item, if any
        # Hard to make this O(1) without making it a circular buffer
        if self.length() == 0:
            raise ValueError("Queue is empty")
        old_front_pos = self.front_position
        if self.length() == 1:
            self.front_position = None
        elif self.front_position == self.length() - 1:
            self.front_position = 0
        else:
            self.front_position += 1



        popped = self.list[old_front_pos]
        self.list[old_front_pos] = None
        self.size -= 1
        return popped

    # def calculate_front(self, new_front=0):
    #     return (self.front + new_front) % len
    #
    # def calculate_back(self):
    #     return (self.front + self.length()) % len


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
# Queue = LinkedQueue
Queue = ArrayQueue
#
