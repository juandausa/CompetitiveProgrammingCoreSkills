from erasing_maximum import eraseMaxValue
from random import randrange, shuffle


def test_stamente_one():
    assert eraseMaxValue([1, 3, 2], 3) == [1, 2]

def test_stamente_two():
    assert eraseMaxValue([4, 1, 4, 2, 4, 3, 4], 7) == [4, 1, 4, 2, 3, 4]

def test_random_with_one_maximum():
    values = []
    for _times in range(randrange(1000)):
        values.clear()
        for _i in range(randrange(2, 100)):
            values.append(randrange(1, 95))
        
        values.append(randrange(96,100))
        n = len(values)
        shuffle(values)
        assert len(eraseMaxValue(values, len(values))) == n-1

def test_random_with_several_maximum_values():
    values = []
    for _times in range(randrange(1000)):
        values.clear()
        for _i in range(randrange(2, 100)):
            values.append(randrange(1, 95))
        maximum = randrange(96,100)
        for _i in range(randrange(3, 10)):
            values.append(maximum)

        n = len(values)
        shuffle(values)
        assert len(eraseMaxValue(values, len(values))) == n-1