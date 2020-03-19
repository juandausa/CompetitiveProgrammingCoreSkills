# -*- coding: utf-8 -*-
from compare_list import compare
import sys


def main():
    n = int(input())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))
    assert len(list_a) == len(list_b) == n
    print(compare(list_a, list_b))


if __name__ == '__main__':
    main()
