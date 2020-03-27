# -*- coding: utf-8 -*-
import sys
from common_sequence import common_sequence


def main():
    n = int(input())
    vector_a = list(map(int, str.split(input())))
    vector_b = list(map(int, str.split(input())))
    assert n == len(vector_a) == len(vector_b)
    print(common_sequence(vector_a, vector_b).values)


if __name__ == '__main__':
    main()
