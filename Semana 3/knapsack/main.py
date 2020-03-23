# -*- coding: utf-8 -*-
from knapsack import calculate_best_items
from item import Item
import sys


def main():

    items_count, weight = map(int, input().split())
    items = []
    for _i in range(items_count):
        item_weight, item_value = map(int, input().split())
        items.append(Item(item_weight, item_value))

    print(calculate_best_items(items, weight))


if __name__ == '__main__':
    main()
