def solve(numbers):
    x = numbers[0]
    y = numbers[1]
    z = numbers[2]
    zIndex = -1
    values = dict({0: 0})
    i = 1
    if (z == 0):
        return 0

    if (x == y and x != z):
        return zIndex

    while (True):
        values[(2*i-1) % 3] = values[(2*i-2) % 3] + x
        values[(2*i) % 3] = values[(2*i-1) % 3] - y
        if (values[(2*i-1) % 3] == z):
            zIndex = 2*i-1
            break

        if (values[(2*i) % 3] == z):
            zIndex = 2*i
            break

        if ((values[(2*i-1) % 3] > 1000 and values[(2*i) % 3] > 1000) or (values[(2*i-1) % 3] < 0 and values[(2*i) % 3] < 0)):
            break
        i += 1

    return zIndex
