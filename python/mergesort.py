arr = [3, 5, 1, 10, 7, 2, 200, 45, 6, 3, 1, 0, 4]


def mergesort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    leftA = mergesort(arr[:mid])
    rightA = mergesort(arr[mid:])

    leftI = 0
    rightI = 0
    idx = 0
    while idx < len(arr):
        if rightI >= len(rightA) or (leftI < len(leftA) and leftA[leftI] <= rightA[rightI]):
            arr[idx] = leftA[leftI]
            leftI += 1
        else:
            arr[idx] = rightA[rightI]
            rightI += 1
        idx += 1

    return arr


print(mergesort(arr))
