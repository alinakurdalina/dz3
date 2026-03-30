class GraphicsCard:
    manufacturer = "NVIDIA"
    series = "RTX"

    def __init__(self, name: str, memory: int, memory_type: str, base_clock: int, boost_clock: int):
        self.name = name
        self.memory = memory
        self.memory_type = memory_type
        self.base_clock = base_clock
        self.boost_clock = boost_clock

    def __str__(self) -> str:
        return (f"Видеокарта: {self.name}\n"
                f"Память: {self.memory} ГБ ({self.memory_type})\n"
                f"Частота: {self.base_clock}–{self.boost_clock} МГц\n"
                f"Производитель: {self.manufacturer}, серия: {self.series}")

    def is_modern(self) -> bool:
        modern_memory_types = ["GDDR6", "GDDR6X", "HBM2", "HBM3"]
        return self.memory_type in modern_memory_types

    def get_performance_index(self) -> int:
        return self.memory * self.boost_clock

    def update_memory_type(self, new_memory_type: str) -> None:
        self.memory_type = new_memory_type
        print(f"Тип памяти обновлён на {self.memory_type}")

    def change_series(self, new_series: str) -> None:
        GraphicsCard.series = new_series
        print(f"Серия видеокарты обновлена на {new_series}")


gpu1 = GraphicsCard(
    name="RTX 4080",
    memory=16,
    memory_type="GDDR6X",
    base_clock=2205,
    boost_clock=2505
)

gpu2 = GraphicsCard(
    name="GT 430",
    memory=1,
    memory_type="GDDR3",
    base_clock=700,
    boost_clock=700
)

print(gpu1)
print(f"Актуальная: {gpu1.is_modern()}")
print(f"Индекс производительности: {gpu1.get_performance_index()}\n")

print(gpu2)
print(f"Актуальная: {gpu2.is_modern()}")
print(f"Индекс производительности: {gpu2.get_performance_index()}\n")

gpu1.update_memory_type("HBM3")
gpu2.change_series("GeForce")
print(f"Обновлённая серия для всех видеокарт: {GraphicsCard.series}")
