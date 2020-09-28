coins = [5, 1, 2]
coins2 = [5, 8]
ammount = 13


def coinChangeMin(coins, am):
    dp = [float('inf')] * (am + 1)
    dp[0] = 0
    for c in coins:
        for i in range(c, am + 1):
            dp[i] = min(dp[i-c] + 1, dp[i])

    return dp[am]


def coinChangeMax(coins, am):
    dp = [0] * (am + 1)
    for c in coins:
        for i in range(c, am + 1):
            dp[i] = max(dp[i-c] + 1, dp[i])

    return dp[am]


def coinChangeExclusive(coins, am):
    dp = [float('inf')] * (am + 1)
    dp[0] = 0

    for c in coins:
        for j in range(am, c-1, -1):
            if dp[j-c] != float('inf'):
                dp[j] = min(dp[j], dp[j-c] + 1)
    return dp[am]


print(coinChangeMin(coins, ammount))
print(coinChangeMax(coins, ammount))
print(coinChangeExclusive(coins, ammount))
