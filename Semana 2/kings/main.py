# -*- coding: utf-8 -*-
from place_kings import place_kings
import sys


def main():
    matrixBounds = list(map(int, input().split()))
    print(place_kings(matrixBounds[0], matrixBounds[1]))


if __name__ == '__main__':
    main()
