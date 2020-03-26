from item_unwind import Item
from knapsack_unwind import calculate_best_items, calculate_used_items_in_knapsack


def test_calculate_for_weight_one():
    items = [Item(1, 1), Item(1, 2), Item(1, 9), Item(2, 80000)]
    assert calculate_best_items(items, 1) == 9


def test_stament_one():
    '''3 5 
        1 3 
        1 2 
        1 1
    '''
    items = [Item(1, 3), Item(1, 2), Item(1, 1)]
    assert calculate_best_items(items, 5) == 6


def test_stament_two():
    '''
        5 10 
        1 4 
        2 5 
        1 2 
        4 6 
        8 12
    '''
    items = [Item(1, 4), Item(2, 5), Item(1, 2), Item(4, 6), Item(8, 12)]
    assert calculate_best_items(items, 10) == 18


def test_stament_three():
    '''
        1 5 
        8 3
    '''
    items = [Item(8, 3)]
    assert calculate_best_items(items, 5) == 0


def test_stament_four():
    '''4 10 
        6 30 
        3 14 
        4 16
        2 9
    '''
    items = [Item(6, 30), Item(3, 14), Item(4, 16), Item(2, 9)]
    assert calculate_best_items(items, 10) == 46


def test_get_items_for_one_element():
    items = [Item(1, 1), Item(1, 2), Item(1, 9), Item(2, 80000)]
    assert calculate_used_items_in_knapsack(items, 1) == [3]


def test_get_items_for_two_elements():
    items = [Item(1, 1), Item(1, 2), Item(1, 9), Item(2, 80)]
    assert calculate_used_items_in_knapsack(items, 3) == [3, 4]


def test_get_items_for_three_elements():
    items = [Item(1, 1000), Item(2, 2), Item(
        1, 900), Item(2, 80), Item(3, 1000), Item(3, 2000)]
    assert calculate_used_items_in_knapsack(items, 6) == [1, 3, 6]
