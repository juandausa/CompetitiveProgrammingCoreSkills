from item import Item

def calculate_best_items(items, max_weight, previous_calculations):
    if (max_weight == 1):
        available_items = list(filter(lambda x: x.weight == 1 and x.quantity > 0, items))
        available_items.sort()
        available_items[-1].quantity -=1
        return available_items[-1].value
    
    return 0
