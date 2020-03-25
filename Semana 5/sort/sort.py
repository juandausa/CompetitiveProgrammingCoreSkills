def minimum_sort(numbers, previous_value = -1, actual_index = 0, T = dict()):
    if (actual_index == (len(numbers)-1)):
        T[(previous_value, actual_index)] = 0
        return T[(previous_value, actual_index)]

    if (previous_value, actual_index) in T: 
        return T[(previous_value, actual_index)]
    
    increment = abs(numbers[actual_index + 1] - numbers[actual_index])
    min_sort_take_next_value = minimum_sort(numbers, numbers[actual_index + 1], actual_index + 1) + increment
    min_sort_leave_value_as_is = minimum_sort(numbers, numbers[actual_index], actual_index + 1)
    if (numbers[actual_index] <= numbers[actual_index + 1]):
        # do nothing, increase actual value up to next value
        T[(previous_value, actual_index)] = min(min_sort_take_next_value, min_sort_leave_value_as_is)
    else:
        # increase netx value up to actual value, decrease actual value
        min_sort_decrease_value = min_sort_leave_value_as_is + increment
        T[(previous_value, actual_index)] = min(min_sort_decrease_value, min_sort_take_next_value)

    print(T)
    return T[(previous_value, actual_index)]
        
