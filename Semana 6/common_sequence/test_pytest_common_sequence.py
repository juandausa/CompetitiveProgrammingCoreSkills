from common_sequence import common_sequence
from random import randrange

def test_statement_one():
    assert common_sequence([1, 2], [1, 2]).values == [1, 2]


def test_statement_two():
    assert common_sequence(
        [1, 2, 3, 4, 5], [1, 3, 2, 4, 4]).values == [1, 3, 4]


def test_statement_three():
    assert common_sequence([1, 2, 3, 3, 4, 6], [
                           1, 6, 3, 3, 2, 4]).values == [1, 3, 3, 4]


def test_statement_four():
    assert common_sequence([1, 2, 3], [1, 2, 3]).values == [1, 2, 3]


def test_statement_five():
    assert common_sequence([1, 2, 3, 3, 4, 6, 1, 2, 3, 3, 4, 6, 1, 2, 3, 3, 4, 6, 1, 2, 3, 3, 4, 6], [
                           1, 6, 3, 3, 2, 4, 1, 6, 3, 3, 2, 4, 1, 6, 3, 3, 2, 4, 1, 6, 3, 3, 2, 4]).values == [1, 3, 3, 4, 1, 3, 3, 4, 1, 3, 3, 4, 1, 3, 3, 4]


def test_large_random_vectors():
    sequence_a = []
    sequence_b = []

    for _i in range(1000):
        sequence_a.append(randrange(1, 1000))
        sequence_b.append(randrange(1, 1000))

    assert common_sequence(sequence_a, sequence_b).len() > 0
