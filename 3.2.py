import math
from statistics import median

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно!")
    return a / b

def power(a, b):
    return a ** b

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Факториал определен только для неотрицательных целых чисел!")
    return math.factorial(n)

def square_root(n):
    if n < 0:
        raise ValueError("Нельзя извлечь корень из отрицательного числа!")
    return math.sqrt(n)

def calculate_median(numbers):
    try:
        numbers = list(map(float, numbers.split()))
        return median(numbers)
    except ValueError:
        raise ValueError("Введите числа через пробел!")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число!")

def main():
    operations = {
        1: add,
        2: subtract,
        3: multiply,
        4: divide,
        5: power,
        6: factorial,
        7: square_root,
        8: calculate_median
    }

    while True:
        print("\nДоступные операции:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Факториал")
        print("7. Квадратный корень")
        print("8. Медиана")
        print("exit - выход")

        choice = input("\nОперация: ")

        if choice.lower() == "exit":
            print("Программа завершена")
            break

        try:
            choice = int(choice)
            if choice not in operations:
                raise ValueError("Неверная операция!")

            if choice in [1, 2, 3, 4, 5]:
                a = get_number("Число 1: ")
                b = get_number("Число 2: ")
                result = operations[choice](a, b)

            elif choice == 6:
                n = int(get_number("Число: "))
                result = operations[choice](n)

            elif choice == 7:
                n = get_number("Число: ")
                result = operations[choice](n)

            elif choice == 8:
                numbers = input("Введите числа через пробел: ")
                result = operations[choice](numbers)

            print(f">>> {result}")

        except Exception as e:
            print(f"Ошибка: {str(e)}")


if __name__ == "__main__":
    main()