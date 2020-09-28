from collections import defaultdict


def dfs(arr, s, mem, sums, subs, curr):
    subs.append(curr)
    if not arr:
        return

    for i in range(len(arr)):
        aux = s + arr[i]
        if aux % 2 != 0 and not sums[aux]:
            mem[0] += 1
        sums[aux] = True
        dfs(arr[i+1:], aux, mem, sums, subs, curr + [arr[i]])


def numOfSubarrays(arr):
    mod = (10**9) + 7
    mem = [0]
    subs = []
    sums = defaultdict(bool)
    dfs(arr, 0, mem, sums, subs, [])
    print(sums)
    return mem[0] % mod


def dp(arr):
    mod = (10**9) + 7
    even, odd = 0, 0
    res = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            res += odd
            even += 1

        if arr[i] % 2 != 0:
            res += even + 1
            odd += 1
    return res


def rotate(nums, k):
    count = 0
    i = 0
    n = len(nums)
    while i < n and count < n:
        startI = i
        currentI = (i + k) % n
        aux = nums[i]
        while True:
            nums[currentI], aux = aux, nums[currentI]
            count += 1

            if currentI == startI:
                break

            currentI = (currentI + k) % n

        i += 1

    return nums


#print(numOfSubarrays([1, 2, 3, 4, 5, 6, 7]))
#print(dp([1, 2, 3, 4, 5, 6, 7]))
print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
