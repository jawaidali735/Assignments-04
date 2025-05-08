def in_range(n, low, high):
    if n >= low and n <= high:
        return True
    return False


def main():
    print(in_range(5, 1, 10))     # True (5 is between 1 and 10)
    print(in_range(1, 1, 10))     # True (1 is exactly low)
    print(in_range(10, 1, 10))    # True (10 is exactly high)
    print(in_range(0, 1, 10))     # False (0 is less than low)
    print(in_range(11, 1, 10))    # False (11 is more than high)

if __name__ == '__main__':
    main()