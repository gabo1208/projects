colorfull = 3245
results = {}

"""
First approach
while(colorfull > 0):
    digits.append(colorfull % 10)
    colorfull = colorfull // 10

for seq_size in range(0, len(digits) - 1):
    for i in range(len(digits) - seq_size):
        mult = 1
        for j in range(i, i + seq_size + 1):
            mult *= digits[j]

        if mult not in results.keys():
            results[mult] = True
        else:
            print('Not colorfull')
            print(results)
            exit()
"""


def getDigitsArray(colorfull):
    digits = []
    while(colorfull > 0):
        digits.append(colorfull % 10)
        colorfull = colorfull // 10
    return digits


def checkIfColorfull(digits):
    results = {}
    for i in range(len(digits)):
        mult = 1
        for j in range(i, len(digits)):
            mult *= digits[j]
            if mult in results.keys():
                print('Not colorfull')
                return results
            else:
                results[mult] = True

    print('Colorfull')
    return results


digits = getDigitsArray(colorfull)
print(checkIfColorfull(digits))
