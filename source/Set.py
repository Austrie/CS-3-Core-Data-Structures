#!python

from linkedlist import LinkedList

class Set(object):
    def __init__(self, iterable = None):
        self.list = LinkedList()
        self.size = 0

        if iterable is not None:
            for item in iterable:
                self.add(item)

    def add(self, item):
        if item is None:
            raise ValueError("Item can not be null")
        if self.contains(item):
            pass
        else:
            self.list.append(item)
            self.size += 1

    def contains(self, item):
        if item is None:
            raise ValueError("Item can not be null")
        def __items_are_equal__(item2):
            if item2 == item:
                return True
        if self.list.find(__items_are_equal__):
            return True
        return False

    def remove(self, item):
        if item is None:
            raise ValueError("Item can not be null")
        return self.list.delete(item)

if __name__ == '__main__':
    set = Set()
    for i in range(5):
        set.add(i)
    print("Set contains 4: {}".format(set.contains(4)))
    set.remove(4)
    print(set.list)
