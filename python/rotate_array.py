test = [1, 2, 3, 4, 5]


def rotate(nums, k):
    k = k % len(nums)
    reverse(nums, 0, len(nums) - 1)
    print(nums)
    reverse(nums, k, len(nums) - 1)
    print(nums)
    reverse(nums, 0, k - 1)
    print(nums)


def reverse(nums, start, end):
    while (start < end):
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start += 1
        end -= 1


rotate(test, 3)
print(test)
