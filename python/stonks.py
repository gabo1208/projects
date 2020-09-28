test = [7, 6, 4, 3, 1]


def maxProfit(prices):
    difference = prices[0]
    toBuyIndex = 0
    toSelIndex = 0
    credit = 0
    for i in range(1, len(prices)):
        if difference - prices[i] > 0:
            toBuyIndex = i
        else:
            toSelIndex = i
        difference = prices[i]

    print(toBuyIndex)
    print(toSelIndex)


def maxProfit2(prices):
    if not prices:
        return 0

    fb, sb = -float('inf'), -float('inf')
    fs, ss = 0, 0

    for price in prices:
        fb = max(fb, -price)
        fs = max(fs, fb + price)
        sb = max(sb, fs - price)
        ss = max(ss, sb + price)

    return ss


test2 = [3, 2, 3]

maxProfit2(test2)
