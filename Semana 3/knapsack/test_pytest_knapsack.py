from item import Item
from knapsack import calculate_best_items


def test_calculate_for_weight_one():
    items = [Item(1,1, 1), Item(1,2, 1), Item(1, 9, 1), Item(2,80000, 1)]
    assert calculate_best_items(items, 1, dict()) == 9