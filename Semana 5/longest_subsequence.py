def longest_subsequence(A, last_index=-1, previous_calculations=dict()):
    if last_index == -1:
        last_element = float("-inf")
    elif last_index in previous_calculations.keys():
        return previous_calculations[last_index]
    else:
        last_element = A[last_index]

    result = 0

    for i in range(last_index + 1, len(A)):
        if A[i] > last_element:
            result = max(result, 1 + longest_subsequence(A, i, previous_calculations))

    previous_calculations[last_index] = result
    return previous_calculations[last_index]


def main():
    sequence = [7, 2, 1, 3, 8, 4, 9, 10, 34, 12, 67, 15, 7, 5, 68, 90, 103]
    print(sequence)
    print(longest_subsequence(sequence))


if __name__ == '__main__':
    main()
