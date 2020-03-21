from occurrence import Occurrence
from copy import copy


class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.value = None
        self.left = None
        self.right = None
        self.childs = end - start + 1


class SegmentTree(object):
    def __init__(self, phrase):
        #helper function to create the tree from input array
        def createTree(phrase, left, right):
            # base case
            if left > right:
                return None

            # leaf node
            if left == right:
                node = Node(left, right)
                node.value = Occurrence(phrase[left], 1)
                return node

            middle = (left + right) // 2
            root = Node(left, right)

            # recursively build the Segment tree
            root.left = createTree(phrase, left, middle)
            root.right = createTree(phrase, middle+1, right)

            # Total stores the sum of all leaves under root
            # i.e. those elements lying between (start, end)
            newValue = copy(root.left.value)
            newValue.add(root.right.value)
            root.value = newValue

            return root

        self.root = createTree(phrase, 0, len(phrase)-1)

    def getMostFrequetCharacter(self, left, right):
        #Helper function to calculate range sum
        def calculateMostrFrequetCharacter(root, left, right):

            #If the range exactly matches the root, we already have the sum
            if root.start == left and root.end == right:
                return root.value

            mid = (root.start + root.end) // 2

            #If end of the range is less than the mid, the entire interval lies
            #in the left subtree
            if right <= mid:
                return calculateMostrFrequetCharacter(root.left, left, right)

            #If start of the interval is greater than mid, the entire inteval lies
            #in the right subtree
            elif left >= mid + 1:
                return calculateMostrFrequetCharacter(root.right, left, right)

            #Otherwise, the interval is split. So we calculate the sum recursively,
            #by splitting the interval
            else:
                leftValues = copy(
                    calculateMostrFrequetCharacter(root.left, left, mid))
                leftValues.add(calculateMostrFrequetCharacter(
                    root.right, mid+1, right))
                return leftValues

        assert left >= 1
        assert right <= self.root.childs
        return calculateMostrFrequetCharacter(self.root, left-1, right-1).get_element_with_maximum_occurrence()
