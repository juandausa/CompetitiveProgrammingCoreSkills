from occurrence import Occurrence
from copy import copy


class SegmentTree:
    def __init__(self, phrase):
        self.tree = build_tree(phrase)
        self.total_elements = len(phrase)

    def query(self, lower, higher):
        return query_tree(self.tree, self.total_elements, lower, higher)


def build_tree(phrase):
    segment_tree = [0] * (2 * len(phrase))
    n = len(phrase)
    # insert leaf nodes in tree
    for i in range(n):
        segment_tree[n + i] = Occurrence(phrase[i], 1)

    # build the tree by calculating parents
    for i in range(n - 1, 0, -1):
        previous_value = copy(segment_tree[i << 1])
        previous_value.add(segment_tree[i << 1 | 1])
        segment_tree[i] = previous_value

    return segment_tree


def query_tree(segment_tree, n, lower, higher):

    result = Occurrence()
    lower += n
    higher += n

    while lower < higher:
        if (lower & 1):
            result.add(segment_tree[lower])
            lower += 1

        if (higher & 1):
            higher -= 1
            result.add(segment_tree[higher])

        lower >>= 1
        higher >>= 1

    return result.get_element_with_maximum_occurrence()
