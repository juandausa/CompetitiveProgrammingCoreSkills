def minimum_sort(numbers, previous_value=-1, actual_index=0, previous_calculation=None):
    if (previous_calculation is None):
        previous_calculation = dict()

    if (actual_index == (len(numbers)-1)):
        previous_calculation[(previous_value, actual_index)] = abs(
            previous_value-numbers[actual_index]) if previous_value > numbers[actual_index] else 0
        return previous_calculation[(previous_value, actual_index)]

    if (previous_value, actual_index) in previous_calculation:
        return previous_calculation[(previous_value, actual_index)]

    increment = abs(numbers[actual_index + 1] - numbers[actual_index])
    min_sort_take_next_value = minimum_sort(
        numbers, numbers[actual_index + 1], actual_index + 1, previous_calculation) + increment
    min_sort_leave_value_as_is = minimum_sort(
        numbers, numbers[actual_index], actual_index + 1, previous_calculation)
    if (numbers[actual_index] <= numbers[actual_index + 1]):
        # do nothing, increase actual value up to next value, descrease actual value down to previous_value
        min_sort_decrease_value_down_to_previous_value = minimum_sort(
            numbers, previous_value, actual_index + 1, previous_calculation) + abs(previous_value-numbers[actual_index])
        previous_calculation[(previous_value, actual_index)] = min(min_sort_take_next_value, min_sort_leave_value_as_is) if previous_value == - \
            1 else min(min_sort_take_next_value, min_sort_leave_value_as_is, min_sort_decrease_value_down_to_previous_value)
    else:
        # numbers[index] > numbers[index + 1]
        # increase next value up to actual value, decrease actual value down to next value
        min_sort_decrease_value = minimum_sort(numbers, )
        previous_calculation[(previous_value, actual_index)] = min(
            min_sort_decrease_value, min_sort_take_next_value)

    return previous_calculation[(previous_value, actual_index)]
