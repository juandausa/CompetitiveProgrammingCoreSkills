from sort import minimum_sort
import sys


def main():
    n = int(input())
    sequence = list(map(int, str.split(input())))
    assert n == len(sequence)
    print(minimum_sort(sequence))


if __name__ == '__main__':
    main()
