def binary_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 0:
        k = n / 2
        return binary_fib(k) * (2 * binary_fib(k + 1) - binary_fib(k))
    else:
        k = (n + 1) / 2
        return binary_fib(k) ** 2 + binary_fib(k - 1) ** 2
    print(binary_fib(10))