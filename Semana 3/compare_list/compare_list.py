

def compare(list_a, list_b):
    sum_a = sum(list_a)
    sum_b = sum(list_b)
    if (sum_a == sum_b):
        return "SUM(A)=SUM(B)"
    elif (sum_a > sum_b):
        return "SUM(A)>SUM(B)"
    
    return "SUM(A)<SUM(B)"
