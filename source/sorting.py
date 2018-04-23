#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if not
    for i in range(0, len(items) - 1):
        if items[i] > items[i + 1]:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(items) - 1):
            if items[i] > items[i + 1]:
                temp = items[i]
                items[i] = items[i + 1]
                items[i + 1] = temp
                swapped = True

    return items



def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    for i in range(0, len(items) - 1):
        minimum = items[i]
        position = i
        for j in range(i + 1, len(items)):
            if minimum > items[j]:
                minimum = items[j]
                position = j
        temp = items[i]
        items[i] = minimum
        items[position] = temp

    return items




def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    if items == []:
        return items
    for i in range(1, len(items)):
        for j in range(0, i):
            print(j)
            # print(lis)
            if items[i] < items[j]:
                temp = items.pop(i)
                items.insert(j, temp)
                break
    return items

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    if items1 == []:
        return items2
    elif items2 == []:
        return items1
    lis = []
    item1 = items1.pop(0)
    item2 = items2.pop(0)
    while item1 != None and item2 != None:
        if item1 < item2:
            lis.append(item1)
            if items1 == []:
                lis.append(item2)
                break
            else:
                item1 = items1.pop(0)
        else:
            lis.append(item2)
            if items2 == []:
                lis.append(item1)
                break
            else:
                item2 = items2.pop(0)

    while items1 != []:
        lis.append(items1.pop(0))
    while items2 != []:
        lis.append(items2.pop(0))
    return lis


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order
    if len(items) < 2:
        return items
    middle = int(len(items) / 2)
    lis1 = insertion_sort(items[0 : middle])
    lis2 = insertion_sort(items[middle : len(items)])
    return merge(lis1, lis2)



def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    if len(items) < 2:
        return items
    elif len(items) is 2:
        if items[0] > items[1]:
            temp = items[0]
            items[0] = items[1]
            items[1] = temp
            return items
        else:
            return items
    else:
        middle = int(len(items) / 2)
        lis1 = items[0 : middle]
        lis2 = items[middle : len(items)]
        lis1 = merge_sort(lis1)
        lis2 = merge_sort(lis2)
        return merge(lis1, lis2)



def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p
    if low > high or low < 0 or high >= len(items):
        return None
    
    middleIndex = ((high - low) // 2) + low
    middleItem = items[middleIndex]
    for i in range(low, high):
        if i == middleIndex:
            continue
        elif items[i] <= middleItem and i > middleIndex:
            middleIndex += 1
            items.insert(0, items.pop(i))
        elif items[i] > middleItem and i < middleIndex:
            middleIndex -= 1
            items.append(items.pop(i))

    return middleIndex


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
    #
    # CHECK NONE HERE
    if low is None or high is None:
        low = 0
        high = len(items) - 1

    print("Items Before: ")
    print(items)

    middleIndex = partition(items, low, high)
    if middleIndex is not None:
        print("Middle: " + str(middleIndex))
    else:
        print("MIDDLE IS NONE")
    print("Low: " + str(low))
    print("High: " + str(high))
    print("Items Now: ")
    print(items)
    if middleIndex is not None:
        quick_sort(items, low, middleIndex - 1)
        quick_sort(items, middleIndex + 1, high)

    # done = False
    # original_middleIndex = middleIndex
    # # Left hand side
    # while not done:
    #     if middleIndex is None:
    #         done = True
    #     else:
    #         new_high = middleIndex - 1
    #         middleIndex = partition(items, low, new_high)
    #
    # done = False
    # middleIndex = original_middleIndex
    # # Right hand side
    # while not done:
    #     if middleIndex is None:
    #         done = True
    #     else:
    #         new_low = middleIndex + 1
    #         middleIndex = partition(items, new_low, high)

    # return items


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    sorting each bucket, and combining contents of all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def test_sorting(sort=bubble_sort, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of items randomly sampled from range [1...max_value]
    items = random_ints(num_items, 1, max_value)
    print('Initial items: {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    sort(items)
    print('Sorted items:  {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('    randomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if name.find('sort') >= 0:
                    print('    {}'.format(name))
            return

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
        # print('Num items: {}, max value: {}'.format(num_items, max_value))
    except ValueError:
        print('Integer required for `num` and `max` command-line arguments')
        return

    # Test sort function
    test_sorting(sort_function, num_items, max_value)


if __name__ == '__main__':
    main()
    # lis = [3,1,6,5,22,3,5,7,0]
    # print(lis)
    # print(bubble_sort(lis))
