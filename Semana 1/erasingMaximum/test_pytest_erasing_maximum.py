from erasingMaximum import eraseMaxValue
from random import randrange


def test_stamente_one():
    assert eraseMaxValue([1, 3, 2], 3) == [1, 2]

def test_stamente_two():
    assert eraseMaxValue([4, 1, 4, 2, 4, 3, 4], 7) == [4, 1, 4, 2, 3, 4]
