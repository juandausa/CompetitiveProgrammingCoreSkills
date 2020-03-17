def eraseMaxValue(values, n):
    if (n < 2):
        raise Exception('Bad input')

    if (len(values) != n):
        raise Exception('Bad input')

    dist = dict()
    max = 0
    for i in range(n):
        if (values[i] in dist.keys()):
            dist[values[i]].append(i)
        else:
            dist[values[i]] = [i]
        if (values[i] > max):
            max = values[i]

    if (len(dist[max]) == 1):
        del values[dist[max][0]]
    elif (len(dist[max]) >= 3):
        del values[dist[max][2]]
    else:
        raise Exception('Bad input')

    return values
