from item import Item


def calculate_best_items(items, max_weight):
    previous_calculations = [
        [0 for _w in range(max_weight + 1)] for _i in range(len(items)+1)]

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
