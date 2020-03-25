from edit_distance import edit_distance


def test_edit_redit():
    assert edit_distance("edit", "redit") == 1


def test_digit_redit():
    assert edit_distance("digit", "redit") == 3


def test_information_applications():
    assert edit_distance("information", "applications") == 7


def test_editing_distance_1_1_100():
    assert edit_distance("editing", "distance", 1, 1, 100) == 7


def test_editing_distance_100_1_1():
    assert edit_distance("editing", "distance", 100, 1, 1) == 105


def test_editing_distance_1_100_1():
    assert edit_distance("editing", "distance", 1, 100, 1) == 6


def test_a_b_100_1_1():
    assert edit_distance("a", "b", 100, 1, 2) == 2


def test_a_bb_100_1_1():
    assert edit_distance("a", "bb", 100, 1, 1) == 101


def test_bc_bbcc_100_1_1():
    assert edit_distance("bc", "bbcc", 100, 1, 1) == 200
