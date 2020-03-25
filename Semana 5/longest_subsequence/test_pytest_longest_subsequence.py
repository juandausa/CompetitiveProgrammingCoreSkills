from longest_subsequence import longest_subsequence


def test_statement_one():
    '''
    6 
    5 3 2 4 6 1
    '''
    assert longest_subsequence([5, 3, 2, 4, 6, 1]) == 3


def test_statement_two():
    '''
    6 
    1 1 2 2 3 3
    '''
    assert longest_subsequence([1, 1, 2, 2, 3, 3]) == 3


def test_statement_three():
    '''
    5
    5 4 3 2 1
    '''
    assert longest_subsequence([5, 4, 3, 2, 1]) == 1

