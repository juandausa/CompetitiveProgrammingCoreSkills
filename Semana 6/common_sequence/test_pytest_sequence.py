from sequence import Sequence


def test_empty_sequence():
    assert Sequence().len() == 0


def test_add_two_empty_sequences():
    empty_a = Sequence()
    empty_b = Sequence()
    sum = empty_a+empty_b
    assert sum.len() == 0


def test_add_two_sequences():
    empty_a = Sequence([1])
    empty_b = Sequence([2])
    sum = empty_a+empty_b
    assert sum.len() == 2
