def arrSum(arr, f, t):
    dp = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        dp[i + 1] = dp[i] + arr[i]
    print(dp)
    return dp[t + 1] - dp[f]


def sumMatrix(m, c1, r1, c2, r2):
    if not m or not m[0]:
        return 0

    n = len(m)
    m = len(m[0])
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            dp[i + 1][j + 1] = dp[i][j+1] + \
                dp[i+1][j] + matrix[i][j] - dp[i][j]
    return dp[r2 + 1][c2 + 1] - dp[r2 + 1][c1] - dp[r1][c2 + 1] + dp[r1][c1]


def countSquares(matrix):
    if not matrix or not matrix[0]:
        return 0

    n = len(matrix)
    m = len(matrix[0])
    count = 0
    for i in range(n):
        count += matrix[i][0]

    for j in range(1, m):
        count += matrix[0][j]

    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j]:
                matrix[i][j] = min(
                    min(matrix[i-1][j], matrix[i][j-1]),
                    matrix[i-1][j-1]
                ) + 1
                count += matrix[i][j]

    print(matrix)

    return count


#print(arrSum([1, 2, 3, 4], 2, 2))
print(countSquares([[1, 0, 1], [1, 1, 0], [1, 1, 0]]))
