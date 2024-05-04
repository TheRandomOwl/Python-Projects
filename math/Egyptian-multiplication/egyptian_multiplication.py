def egyptian_multiplication(a, b):
    """
    Performs Egyptian multiplication of two numbers.

    >>> egyptian_multiplication(13, 24)
    halve 13, double 24
    halve 6, double 48
    halve 3, double 96
    halve 1, double 192
    add [24, 96, 192]
    Answer: 312

    >>> egyptian_multiplication(-12, 5)
    halve -12, double 5
    halve -6, double 10
    halve -3, double 20
    halve -1, double 40
    add [-20, -40]
    Answer: -60

    >>> egyptian_multiplication(16, 26)
    halve 16, double 26
    halve 8, double 52
    halve 4, double 104
    halve 2, double 208
    halve 1, double 416
    add [416]
    Answer: 416
    """

    ans = []
    while abs(a) >= 1 and abs(a) > 0:
        if (a % 2 != 0 and a > 0):
            ans.append(b)
        elif (a % 2 != 0 and a < 0):
            ans.append(-b)
        print(f"halve {a}, double {b}")
        a = int(a/2)
        b *= 2
    print(f"add {ans}")
    print(f"Answer: {sum(ans)}")

def main():
    egyptian_multiplication(102, -5)

if __name__ == "__main__":
    main()
    # import doctest
    # doctest.testmod()