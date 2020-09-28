def factorial(n):
    f = 1
    i = 1
    while i <= n:
        f *= i
        print(str(i) + ': ' + str(f))
        i += 1
    return f


factorial(20)
