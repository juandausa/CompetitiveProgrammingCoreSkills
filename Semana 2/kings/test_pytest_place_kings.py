from place_kings import place_kings, is_free


def test_is_free_empty_board():
    places = [[False for x in range(2)] for y in range(2)]
    assert is_free(0, 0, places)
    assert is_free(0, 1, places)
    assert is_free(1, 0, places)
    assert is_free(1, 1, places)


def test_is_free_outside_board():
    places = [[False for x in range(2)] for y in range(2)]
    assert not is_free(-1, 0, places)
    assert not is_free(0, -1, places)
    assert not is_free(2, 0, places)
    assert not is_free(0, 2, places)

def test_is_free_within_full_board():
    places = [[True for x in range(2)] for y in range(2)]
    assert not is_free(1, 0, places)
    assert not is_free(0, 1, places)
    assert not is_free(1, 0, places)
    assert not is_free(1, 1, places)


def test_stamente_one():
    assert place_kings(1, 2) == 1


def test_stamente_two():
    assert place_kings(3, 3) == 8

