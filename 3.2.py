def add(a, b): return a + b


def sub(a, b): return a - b


def mul(a, b): return a * b


def div(a, b):
    if b == 0: raise ZeroDivisionError("На ноль делить нельзя")
    return a / b


def pow_(a, b): return a ** b


def fact(n):
    if not isinstance(n, int) or n < 0: raise ValueError("Факториал только для целых чисел >=0")
    return 1 if n == 0 else n * fact(n - 1)


def sqrt_(n):
    if n < 0: raise ValueError("Корень из отрицательного числа")
    return n ** 0.5


def avg(nums):
    if not nums: raise ValueError("Список пуст")
    for x in nums:
        if not isinstance(x, (int, float)): raise TypeError("Все элементы должны быть числами")
    return sum(nums) / len(nums)


ops = {
    '1': ('+', add, 2), '2': ('-', sub, 2), '3': ('*', mul, 2), '4': ('/', div, 2),
    '5': ('^', pow_, 2), '6': ('!', fact, 1), '7': ('√', sqrt_, 1), '8': ('avg', avg, 'list')
}

while True:
    print("\n1.+ 2.- 3.* 4./ 5.^ 6.! 7.√ 8.avg 0.exit")
    c = input("Выбор: ").strip()
    if c in ('0', 'exit'): break
    if c not in ops: print("Ошибка"); continue

    try:
        if c == '8':
            nums = [float(x) for x in input("Числа через пробел: ").split()]
            print("=", avg(nums))
        elif c == '6':
            n = int(input("Число: "))
            print("=", fact(n))
        elif c == '7':
            n = float(input("Число: "))
            print("=", sqrt_(n))
        else:
            a = float(input("a: "))
            b = float(input("b: "))
            print("=", ops[c][1](a, b))
    except Exception as e:
        print("Ошибка:", e)
