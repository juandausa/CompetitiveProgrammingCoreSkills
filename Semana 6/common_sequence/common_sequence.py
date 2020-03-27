from sequence import Sequence
import sys

def common_sequence(vector_a, vector_b, index_a=None, index_b=None, T=None):
    sys.setrecursionlimit(10**6) 
    if (index_a is None and index_b is None and T is None):
        return common_sequence(vector_a, vector_b, 1, 1, create_dict())

    if (index_a > len(vector_a) or index_b > len(vector_b)):
        return Sequence()

    if ((index_a, index_b) in T):
        return T[(index_a, index_b)]
    else:
        T[(index_a, index_b)] = Sequence()

    if vector_a[index_a-1] == vector_b[index_b-1]:
        incremented_value = Sequence(
            [vector_a[index_a-1]]) + common_sequence(vector_a, vector_b, index_a+1, index_b+1, T)
        T[(index_a, index_b)] = max(T[(index_a, index_b)], incremented_value)
    else:
        T[(index_a, index_b)] = max(T[(index_a, index_b)], common_sequence(vector_a, vector_b, index_a+1, index_b, T),
                        common_sequence(vector_a, vector_b, index_a, index_b + 1, T))

    return T[(index_a, index_b)]


def create_dict():
    return dict({(0, 0): Sequence(), (0, 1): Sequence(), (1, 0): Sequence()})
