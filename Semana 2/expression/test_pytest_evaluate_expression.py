from evaluate_expression import evaluate_expression

def test_statement_one():
    assert evaluate_expression("1+2+3+4") == 10


def test_statement_one_with_trailspaces():
    assert evaluate_expression(" 1 + 2 + 3 + 4 ") == 10


def test_statement_two():
    assert evaluate_expression("1-2+3-4") == -2


def test_statement_two_with_trailspaces():
    assert evaluate_expression(" 1 - 2 + 3 - 4 ") == -2


def test_sum_several_integers():
    expresion = "+".join([str(x) for x in range(2001)])
    assert evaluate_expression(expresion) == int(2000/2*(2000+1))


def test_substract_several_integers():
    expresion = "-".join([str(x) for x in range(2001)])
    assert evaluate_expression(expresion) == -2000/2*(2000+1)

def test_complex_expression():
    expresion = "1+2+3+4-5-6-6+3+1+4+7-8-8-9-9+6+5-1+2+4-7-4-5+2+1-1-2+3+12-100"
    assert evaluate_expression(expresion) == -111

