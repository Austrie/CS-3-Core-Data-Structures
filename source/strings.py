#!python

''' This method is O(N)'''
def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    return (False if (find_index(text, pattern) is None) else True)

''' This method is O(N)'''
def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    if pattern is "":
        return 0

    i2 = 0
    index = None
    for i in range(0, len(text)):
        a = text[i]
        b = pattern[i2]
        if a is b:
            i2 += 1
            if i2 is len(pattern):
                index = i - i2 + 1
                break
        else:
            i2 = 0
            b = pattern[i2]
            if a is b:
                i2 += 1
                if i2 is len(pattern):
                    index = i - i2 + 1
                    break
            else:
                i2 = 0

    return index

''' This method is O(N)'''
def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    indexes = []
    if pattern is "":
        for i in range(0, len(text)):
            indexes.append(i)
        return indexes

    i2 = 0
    for i in range(0, len(text)):
        a = text[i]
        b = pattern[i2]
        if a is b:
            i2 += 1
            if i2 is len(pattern):
                indexes.append(i - i2 + 1)
                i2 = 0
                b = pattern[i2]
                if len(pattern) > 1 and a is b:
                    i2 += 1
        else:
            i2 = 0
            b = pattern[i2]
            if a is b:
                i2 += 1
                if i2 is len(pattern):
                    index = i - i2 + 1
                    break
            else:
                i2 = 0

    return indexes


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
