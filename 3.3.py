def function(search: str, status: bool, *args: tuple, **kwargs: dict) -> list | str:

    """
    Функция обрабатывает аргументы в зависимости от параметров search и status.

    Args:
        search (str): Строка, определяющая режим обработки аргументов.
            Допустимые значения: "args" или "kwargs".
        status (bool): Флаг, определяющий логику обработки аргументов при search == "args".
            Если True — добавляются только целые числа из *args в результат.
            Если False — все элементы из *args конкатенируются в строку.
        *args (tuple): Переменное количество позиционных аргументов для обработки
            (используется при search == "args").
        **kwargs (dict): Переменное количество именованных аргументов для обработки
            (используется при search == "kwargs").

    Returns:
        list или str:
            - Если search == "args" и status == True: список целых чисел из *args.
            - Если search == "args" и status == False: строка, составленная из элементов *args.
            - Если search == "kwargs": строка с перечислением пар "ключ-значение" из **kwargs.

    Raises:
        ValueError: Если значение search не равно "args" или "kwargs".
    """

    result: list = []
    result_2: str = ""

    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += f"Key: {k}, Value: {v}; "
        return result_2
    else:
        raise ValueError("Error for search")


print(function("args", True, 1, 2, "Три", 4, "Пять"))

print(function("args", False, 1, 2, "Три", 4, "Пять"))

print("Компьютер:", function("kwargs", True, процессор="Intel", память="16GB", диск="SSD"))
