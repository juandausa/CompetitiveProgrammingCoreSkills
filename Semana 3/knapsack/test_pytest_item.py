from item import Item

def test_get_performance():
    assert Item(10, 10).get_performace() == 1
    assert Item(10, 1).get_performace() == 1/10
    assert Item(20, 10).get_performace() == Item(2, 1).get_performace()

def test_sort():
    sorted_items = [Item(1,1), Item(1,2), Item(5, 1), Item(4, 800)]
    sorted_items.sort()
    assert sorted_items[-1].get_performace() == 200