def power(a, n):
    res = 1

    if n > 0:
        for i in range(int(n)):
            res *= a
        return res
    elif n < 0:
        for i in range(abs(int(n))):
            res *= a
        return 1 / res
    else:
        return res


a, n = [float(input()) for i in range(2)]

print(power(a, n))