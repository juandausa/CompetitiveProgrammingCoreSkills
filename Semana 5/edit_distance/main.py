from edit_distance import edit_distance
import sys


def main():
    start, end = str.split(input())
    print(edit_distance(start, end))


if __name__ == '__main__':
    main()
