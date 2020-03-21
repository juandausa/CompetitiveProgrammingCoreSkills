from occurrence import Occurrence
from most_frequent import SegmentTree


def test_create_empty():
    assert Occurrence() is not None


def test_get_occurrence_from_empty():
    oc = Occurrence()
    assert oc.get_occurrence("a") == 0


def test_get_occurrence():
    oc = Occurrence("a", 1)
    assert oc.get_occurrence("a") == 1


def test_add_occurrences_without_intersection():
    oc_a = Occurrence("a", 1)
    oc_b = Occurrence("b", 1)
    oc_a.add(oc_b)
    assert oc_a.get_occurrence("a") == 1
    assert oc_a.get_occurrence("b") == 1


def test_add_occurrences_with_intersection():
    oc_a = Occurrence("b", 10)
    oc_b = Occurrence("b", 1)
    oc_a.add(oc_b)
    assert oc_a.get_occurrence("b") == 11


def test_stament_one():
    '''
    3 
    1 1 a 
    1 7 a
    2 4 b
    '''
    tree = SegmentTree("abacaba")
    assert tree.getMostFrequetCharacter(1, 1) == "a"
    assert tree.getMostFrequetCharacter(2, 2) == "b"
    assert tree.getMostFrequetCharacter(1, 7) == "a"
    assert tree.getMostFrequetCharacter(2, 4) == "b"


def test_stament_two():
    '''
    3 
    1 1 
    2 2 
    1 2 
    2 3 
    1 1 
    2 4
    '''
    tree = SegmentTree("abba")
    assert tree.getMostFrequetCharacter(1, 1) == "a"
    assert tree.getMostFrequetCharacter(2, 2) == "b"
    assert tree.getMostFrequetCharacter(1, 2) == "a"
    assert tree.getMostFrequetCharacter(2, 3) == "b"
    assert tree.getMostFrequetCharacter(2, 4) == "b"
