# (0),1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
def fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(9))

