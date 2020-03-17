# -*- coding: utf-8 -*-
from erasing_maximum import eraseMaxValue
import sys


def main():
    n = int(input())
    a = list(map(int, input().split()))
    result = eraseMaxValue(a, n)
    print(" ".join(map(str, result)))


if __name__ == '__main__':
    main()
