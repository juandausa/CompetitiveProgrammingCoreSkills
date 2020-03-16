# -*- coding: utf-8 -*-

from additionAndSubtraction import solve
import time
import sys


def main():
    #startClock = time.time()
    #print(solve(getInput()))
    #stopClock = time.time() - startClock
    #print("Elapsed time: ", stopClock)
    values = input("Enter 'x' 'y' 'z': ")
    print(solve(list(map(int, values.split()))))


if __name__ == '__main__':
    main()
