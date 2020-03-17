from rank import Rank

def test_A_equals():
    assert Rank("A") == Rank("A")

def test_2_equals():
    assert Rank("2") == Rank("2")

def test_10_equals():
    assert Rank("10") == Rank("10")

def test_J_equals():
    assert Rank("J") == Rank("J")

def test_Q_equals():
    assert Rank("Q") == Rank("Q")

def test_K_equals():
    assert Rank("K") == Rank("K")

def test_sort():
    [Rank("2"), Rank("Q"), Rank("A"), Rank("4")].sort() == [Rank("A"), Rank("2"), Rank("4"), Rank("Q")]