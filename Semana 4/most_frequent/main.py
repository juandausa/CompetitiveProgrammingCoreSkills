from most_frequent import SegmentTree
import sys


if __name__ == "__main__":
    main()


def main():
    phrase = input()
    # build tree
    segment_tree = SegmentTree(phrase)
    limit = list(map(int, str.split(input())))
    assert len(limit) == 2
    print(segment_tree.getMostFrequetCharacter(limit[0], limit[1]))
