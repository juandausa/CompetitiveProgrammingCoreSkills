from item_unwind import Item


def calculate_used_items_in_knapsack(items, max_weight):
    calculations = initialize(items, max_weight)
    calculate_best_items(items, max_weight, calculations)
    return get_items(items, max_weight, calculations)


def initialize(items, max_weight):
    calculations = [
        [0 for _w in range(max_weight + 1)] for _i in range(len(items)+1)]
    return calculations


def get_items(items, max_weight, calculations):
    i = len(items)
    w = max_weight
    used_items = []
    while (w > 0 and i >= 1):
        if (calculations[i][w] == calculations[i-1][w]):
            i -= 1
        else:
            used_items.append(i)
            i -= 1
            w -= items[i].weight

    used_items.reverse()
    return used_items


def calculate_best_items(items, max_weight, previous_calculations = None):
    if (previous_calculations is None):
        previous_calculations = initialize(items, max_weight)
    
    for actual_elements in range(1, len(previous_calculations)):
        for actual_weight in range(1, len(previous_calculations[actual_elements])):
            previous_calculations[actual_elements][actual_weight] = previous_calculations[actual_elements - 1][actual_weight]

            if(items[actual_elements - 1].weight > actual_weight):
                continue

            candidate_value = get_candidate(
                items, previous_calculations, actual_elements, actual_weight)
            if(candidate_value > previous_calculations[actual_elements][actual_weight]):
                previous_calculations[actual_elements][actual_weight] = candidate_value

    return previous_calculations[len(items)][max_weight]


def get_candidate(items, previous_calculations, actual_elements, actual_weight):
    return previous_calculations[actual_elements - 1][actual_weight - items[actual_elements - 1].weight] + items[actual_elements - 1].value
