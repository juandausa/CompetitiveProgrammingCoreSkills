from sort import minimum_sort


def test_statement_one():
    '''
    3
    1 2 1
    '''
    assert minimum_sort([1,2,1]) == 1


def test_statement_two():
    '''
    2
    5 10
    '''
    assert minimum_sort([5, 10]) == 0


def test_statement_three():
    '''
    7
    1 4 2 3 1 4 4
    '''
    assert minimum_sort([1, 4, 2, 3, 1, 4, 4]) == 4


def test_statement_four():
    '''
    10
    10 9 8 7 6 5 4 3 2 1
    '''
    assert minimum_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9


def test_statement_five():
    '''
    3
    10 9 8
    '''
    assert minimum_sort([10, 9, 8]) == 2


def test_statement_six():
    '''
    30
    10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2 1
    '''
    assert minimum_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 27


def test_statement_seven():
    '''
    3
    10 9 8 7
    '''
    assert minimum_sort([10, 9, 8, 7]) == 3
