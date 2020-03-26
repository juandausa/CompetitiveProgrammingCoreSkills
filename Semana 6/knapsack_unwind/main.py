# -*- coding: utf-8 -*-
from knapsack_unwind import calculate_used_items_in_knapsack
from item_unwind import Item
import sys


def main():

    items_count, weight = map(int, input().split())
    items = []
    for _i in range(items_count):
        item_weight, item_value = map(int, input().split())
        items.append(Item(item_weight, item_value))

    used_items = calculate_used_items_in_knapsack(items, weight)
    print(len(used_items))
    print(*used_items, sep = " ")  


if __name__ == '__main__':
    main()
