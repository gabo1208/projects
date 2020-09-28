test = [3, 0, 1]


def missingNumber(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i-1] != nums[i] - 1:
            return i


def aux(nums, l, r):
    if l >= r:
        return
    pivot = nums[(r + l) // 2]
    index = partition(nums, l, r, pivot)
    aux(nums, l, index - 1)
    aux(nums, index, r)


def partition(arr, l, r, pivot):
    while l <= r:
        while arr[l] < pivot and l < len(arr):
            l += 1

        while arr[r] > pivot and r >= 0:
            r -= 1

        if l <= r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    return l


def quicksort(nums):
    aux(nums, 0, len(nums) - 1)
    return nums


print(quicksort(test))
print(missingNumber(test))
