from compare_list import compare

def test_statement_one():
    assert compare([1500, 1500], [1000, 2000]) == "SUM(A)=SUM(B)"


def test_statement_two():
    assert compare([2000], [1123]) == "SUM(A)>SUM(B)"


def test_statement_three():
    assert compare([1000, 2000, 3000], [1001, 2001, 3001]) == "SUM(A)<SUM(B)"


def test_statement_minimum_and_maximum_values():
    assert compare([1000, 2000, 3000, 0.001], [1000, 2000, 3000, 0]) == "SUM(A)>SUM(B)"

