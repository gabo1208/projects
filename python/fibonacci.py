def fibonacci(n, mem):
    if n < 0:
        return 0

    if n < 2:
        mem[n] = n
        return n

    if mem.get(n, -1) < 0:
        mem[n] = fibonacci(n - 1, mem) + fibonacci(n - 2, mem)
        print('saving in mem ' + str(n))
    else:
        print('hit ' + str(n))

    return mem[n]


def go(n, a, b):
    if n == 0:
        return a
    if n == 1:
        return b

    return go(n - 1, b, a + b)


def fibonacciTail(n):
    return go(n, 0, 1)


print(fibonacci(17, {}))
print(fibonacciTail(17))
