# -*- coding: utf-8 -*-
from straight_flush import straight_flush
import sys


def main():
    cards = input().split(" ")
    print(straight_flush(cards))


if __name__ == '__main__':
    main()
