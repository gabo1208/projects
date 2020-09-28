test = [1, 4, 5, 2, 3, 1, 10]


def pairs(arr):
    pairs = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            pairs.append((arr[i], arr[j]))
    return pairs


print(pairs(test))
