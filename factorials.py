def factorial(n):
    t = 1
    for i in range(n):
        n = n * int(factorial(n - 1))
    return n


print(factorial(5))
