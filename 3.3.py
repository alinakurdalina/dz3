def function(search: str, status: bool, *args: tuple, **kwargs: dict) -> list | str:

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

