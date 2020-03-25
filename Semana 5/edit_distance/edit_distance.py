def edit_distance(a, b, add_cost=1, remove_cost=1, replace_cost=1):
    T = initialize(a, b, add_cost, remove_cost)
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            diff = 0 if a[i - 1] == b[j - 1] else replace_cost
            T[i][j] = min(T[i - 1][j] + remove_cost, T[i][j - 1] +
                          add_cost, T[i - 1][j - 1] + diff)

    return T[len(a)][len(b)]


def initialize(a, b, add_cost, remove_cost):
    T = [[float("inf")] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a) + 1):
        T[i][0] = remove_cost * i
    for j in range(len(b) + 1):
        T[0][j] = add_cost * j

    return T
