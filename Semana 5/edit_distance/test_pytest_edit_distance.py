from edit_distance import edit_distance


def test_edit_redit():
    assert edit_distance("edit", "redit") == 1


def test_digit_redit():
    assert edit_distance("digit", "redit") == 3


def test_information_applications():
    assert edit_distance("information", "applications") == 7

