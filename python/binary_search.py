t = [-10, -2, -1, 1, 3]


def binarySearch(arr, pos):
    l = 0
    r = len(arr)
    while l < r:
        m = (l + r) // 2
        if pos < arr[m]:
            r = m
        elif pos > arr[m]:
            l = m + 1
        else:
            return m
    return l


def findMin():
    a = [2, 3, 4, 5, 1]
    l = 0
    r = len(a)
    while l < r:
        m = (l + r) // 2
        if m == [0] or a[m] < a[m-1]:
            return m
        elif a[m] > a[len(a) - 1]:
            l = m + 1
        else:
            r = m
    return l

# get first and last indexes of an ocurrence in an ordered array

# get min in a shifted sorted array

# find in rotated sorted array


print(binarySearch(t, 0))
print(findMin())
