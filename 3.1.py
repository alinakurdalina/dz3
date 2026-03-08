numbers = [int(x) for x in input("Введите список чисел через пробел: ").split()]
multiplier_input = input("Введите множитель: ")

multiplier = int(multiplier_input) if multiplier_input.strip() != '' else 2
def multiply_list(elements: list[int], mult: int = 2) -> list[int]:
    result = []
    for item in elements:
        result.append(item * mult)
    return result

multiply_lambda = list(map(lambda x: x * multiplier, numbers))

print(f"Результат (функция): {multiply_list(numbers, multiplier)}")
print(f"Результат (лямбда-функция): {multiply_lambda}")