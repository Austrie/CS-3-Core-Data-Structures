#!python

### MAJOR THANKS TO AAKASH FOR HELP WITH THIS

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


# TODO: Try recursive solution
def decode(digits, base):
    # Handle up to base 36 [0-9a-z]
    assert (2 <= base <= 36), "\nBASE IS OUT-OF-RANGE: {}\n".format(base)

    # Creates dictionary of possible base conversion digits
    base_conversion_dict, iterator, base_sum = dict(), 0, 0
    for item in (string.digits + string.ascii_lowercase):
        base_conversion_dict[item] = iterator
        iterator += 1

    # Iterates through digit string and converts into base power sum in base 10
    for index, digit in enumerate(str(digits)[::-1]):
        base_sum += int(base_conversion_dict[digit]) * (base ** index)
    return base_sum

    # return sum([(int(base_conversion_dict[digit]) * (base ** index)) for index, digit in enumerate(str(digits)[::-1])])


# TODO: Try iterative solution
def encode(number, base):
    # Handle up to base 36 [0-9a-z] and unsigned numbers only for now
    assert (2 <= base <= 36), "\nBASE IS OUT OF RANGE: {}\n".format(base)
    assert number >= 0, "\nNUMBER IS NEGATIVE: {}\n".format(number)

    base_list = string.digits + string.ascii_lowercase
    if number < base:
        return base_list[number]
    else:
        return encode(number // base, base) + base_list[number % base]


def convert(digits, base_original, base_final):
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base_original <= 36, "\nORIGINAL BASE IS OUT OF RANGE: {}\n".format(base_original)
    assert 2 <= base_final <= 36, "\nFINAL BASE IS OUT OF RANGE: {}\n".format(base_final)

    return encode(decode(digits, base_original), base_final)


def test_decode():
    # Testing decode()
    args = sys.argv[1:]
    if len(args) == 2:
        digits = args[0].lower()
        base = int(args[1])
        result = decode(digits, base)
        print("\n{} IN BASE {} IS {} IN BASE 10\n".format(digits, base, result))
    else:
        print("\nUSAGE: {} [digits] [base]".format(sys.argv[0]))
        print("DECODES [digits] FROM [base] TO BASE 10\n")


def test_encode():
    # Testing encode()
    args = sys.argv[1:]
    if len(args) == 2:
        digits, base = int(args[0]), int(args[1])
        result = encode(digits, base)
        print("\n{} IN BASE 10 IS {} IN BASE {}\n".format(digits, result.upper(), base))
    else:
        print("\nUSAGE: {} [digits] [base]".format(sys.argv[0]))
        print("ENCODES [digits] FROM BASE 10 TO [base]\n")


def test_convert():
    # Testing convert()
    args = sys.argv[1:]
    if len(args) == 3:
        digits = args[0]
        base_original = int(args[1])
        base_final = int(args[2])
        result = convert(digits, base_original, base_final)         # Convert given digits between bases
        print("\n{} IN BASE {} IS {} IN BASE {}\n".format(digits, base_original, result.upper(), base_final))
    else:
        print("\nUSAGE: {} [digits] [base_original] [base_final]".format(sys.argv[0]))
        print("CONVERTS [digits] FROM [base_original] TO [base_final]\n")

# ====================================== MAIN RUN FUNCTION =======================================
def main():
    # test_decode()
    # test_encode()
    test_convert()


if __name__ == "__main__":
    main()
