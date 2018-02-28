#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)

def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if index == len(array):
        return False

    if array[index] == item:
        return True

    linear_search_recursive(array, item, index + 1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    print("Binary called")
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    array = sorted(array)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # Need to implement case for properly accounting for null spots in array
    print(array)
    end = len(array) - 1
    start = 0
    # The middle is the difference between the start an the end, added to the start
    # or instead of added to the start, subtracted from the end
    middleNum = int((end - start) / 2) + start
    found = False
    print("MiddleNum: {}".format(middleNum))
    while not found:
        # Case: None spots in array
        if array[middleNum] == None:
            raise ValueError("There cant be null spots in array")

        # Case: There are only two items left
        if start is end:
            if array[start] == item:
                return start
            else:
                return None


        middleNum = start + int((end - start) / 2)

        # Case: The item is the middle point
        if array[middleNum] == item:
            return middleNum

        # Case: There are more than two items
            # Item is potentially on the left side of array
        if array[middleNum] > item:
            end = middleNum - 1

            # Item is potentially on the right side of array
        else:
            start = middleNum + 1

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    if item is None or not isinstance(array, list):
        raise ValueError("Neither item nor array cannot be null")
    if left is None or not isinstance(left, int):
        left = 0
    if right is None or not isinstance(right, int):
        right = len(array) - 1

    middleNum = int((right - left) / 2) + left

    # Case: There are None spots in the array
    if array[middleNum] == None:
        raise ValueError("There cant be null spots in array")

    # Case: The item is the middle point
    if array[middleNum] == item:
        return middleNum

    # Case: There are only two items left
    if left is right:
        if array[left] == item:
            return left
        else:
            return None

    # Case: There are more than two items left
        # Item is potentially on the left side
    if array[middleNum] > item:
        return binary_search_recursive(array, item, left, middleNum - 1)

        # Item is potentially on the right side of array
    else:
        return binary_search_recursive(array, item, middleNum + 1, right)
