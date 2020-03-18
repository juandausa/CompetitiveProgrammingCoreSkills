

def evaluate_expression(expression):
    plus_expressions = list(map(str.strip, expression.split('+')))
    processed_expressions = list(map(resolve_minus_expression, plus_expressions))
    return sum(processed_expressions)


def resolve_minus_expression(minus_expression):
    if ("-" not in minus_expression):
        return int(minus_expression)
    
    atomic_minus_expressions = list(map(int, minus_expression.split('-')))
    first_value = int(atomic_minus_expressions.pop(0))
    return first_value - sum(atomic_minus_expressions)