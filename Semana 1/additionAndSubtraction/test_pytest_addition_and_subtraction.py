from additionAndSubtraction import solve
from random import randrange


def test_stamente_one():
    assert solve([2, 0, 3]) == -1


def test_stament_two():
    assert solve([2, 1, 3]) == 3


def test_lower_limits():
    assert solve([0, 0, 0]) == 0


def test_higher_limits():
    assert solve([1000, 0, 1000]) == 1


def test_higher_limits_without_occurrence():
    assert solve([1000, 0, 1]) == -1


def test_special_case():
    assert solve([322, 747, 3]) == -1


def test_special_case_2():
    assert solve([433, 423, 340]) == 68


def test_special_case_3():
    assert verify_solution([948, 944, 712], 356)


def test_special_case_4():
    assert solve([10, 10, 50]) == -1


def test_special_case_5():
    assert verify_solution([10, 10, 10], 1)


def test_random():
    for _i in range(1000):
        x = randrange(1000)
        y = randrange(1000)
        z = randrange(1000)
        zIndex = solve([x, y, z])
        assert verify_solution([x, y, z], zIndex)


def verify_solution(values, calculated_result):
    if (calculated_result == -1):
        return True
    return calculate_value(values[0], values[1], calculated_result) == values[2]


def calculate_value(x, y, zIndex):
    calculated_values = dict({0: 0})
    for i in step_range(2, zIndex+2, lambda x: x + 2):
        calculated_values[(i - 1) % 3] = calculated_values[(i - 2) % 3] + x
        calculated_values[i % 3] = calculated_values[(i - 1) % 3] - y

    return calculated_values[zIndex % 3]


def step_range(start, end, func):
    while start <= end:
        yield start
        start = func(start)
