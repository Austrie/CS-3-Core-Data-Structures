#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        return True if self.list.size is 0 else False

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return self.list.size

    ''' This function is O(1) '''
    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Insert given item
        self.list.prepend(item)

    ''' This function is O(1) '''
    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        if self.length() is 0:
            return None
        else:
            return self.list.head.data

    ''' This function is O(1) '''
    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return top item, if any
        if self.length() is 0:
            raise ValueError("Stack is empty!")
        else:
            data = self.list.head.data
            self.list.delete(data)
            return data


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    ''' This function is O(1) '''
    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        return True if len(self.list) is 0 else False

    ''' This function is O(1) '''
    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return len(self.list)

    ''' This function is amortized O(1) '''
    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Insert given item
        self.list.append(item)

    ''' This function is O(1) '''
    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        if self.length() is 0:
            return None
        else:
            item = self.list[self.length() - 1]
            return item

    ''' This function is O(1) '''
    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return top item, if any
        if self.length() is 0:
            raise ValueError("Stack is empty!")
        return self.list.pop()


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack
