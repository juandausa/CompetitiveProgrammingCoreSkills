from most_frequent import build_tree, query_tree

def main():
    phrase = input()
    # build tree
    segment_tree = build_tree(phrase)
    n = len(phrase)
    limit = list(map(int, str.split(input())))
    assert len(limit) == 2
    print(query_tree(segment_tree, n, limit[0], limit[1]))


# Driver Code
if __name__ == "__main__":
    main()