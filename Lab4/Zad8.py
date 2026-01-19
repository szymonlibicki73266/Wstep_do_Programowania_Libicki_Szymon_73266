def potega(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    return a * potega(a, n - 1)