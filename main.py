def binary_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return binary_fib(n-1) + binary_fib(n-2)
    print(binary_fib(10))