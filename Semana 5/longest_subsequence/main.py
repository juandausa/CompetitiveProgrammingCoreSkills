from longest_subsequence import longest_subsequence
import sys

def main():
    n = int(input())
    sequence = list(map(int, str.split(input())))
    assert n == len(sequence)
    print(longest_subsequence(sequence))


if __name__ == '__main__':
    main()
