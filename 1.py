from Tools.demo.beer import n


def is_prime(x):
    f = True
    for i in range(2, int(x ** 0.5)):
        if x % i == 0:
            f = False
        return (f)


a = int(input("ввести число: "))
print(is_prime)


def check_date(d, m, y):
    if d < 0 or m < 0 or n < 0:
        return False
    mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if y % 400 == 0 or ((y % 4 == 0) and (y % 100 != 0)):
        mon[1] = 29
    if m >= 1 and m <= 12:
        if d > 0 and d <= mon[m - 1]:
            return True
    return False
