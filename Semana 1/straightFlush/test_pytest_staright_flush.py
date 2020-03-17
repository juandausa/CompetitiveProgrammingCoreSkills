from straight_flush import straight_flush

def test_stamente_one():
    assert straight_flush(["2D", "5D", "3D", "4D", "6D"])

def test_stamente_two():
    assert not straight_flush(["AD", "KH", "QH", "JS", "TC"])

def test_differents_suits():
    assert not straight_flush(["2D", "5H", "3D", "4H", "6D"])

def test_same_suits_but_not_stright():
    assert not straight_flush(["2D", "5D", "3D", "4D", "7D"])

def test_same_suits_but_not_stright_with_as():
    assert not straight_flush(["AD", "5D", "3D", "4D", "7D"])

def test_same_suits_with_as_between_K_and_2():
    assert not straight_flush(["AD", "KD", "QD", "2D", "JD"])

def test_same_suits_with_as_as_ending():
    assert straight_flush(["AD", "KD", "QD", "10D", "JD"])

def test_same_suits_with_as_as_begining():
    assert straight_flush(["AD", "2D", "4D", "3D", "5D"])

