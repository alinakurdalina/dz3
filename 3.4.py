class GraphicsCard:
    def __init__(self, name: str, memory: int, memory_type: str,
                 base_clock: int, boost_clock: int):
        self.name = name
        self.memory = memory
        self.memory_type = memory_type
        self.base_clock = base_clock
        self.boost_clock = boost_clock

    def __str__(self):
        return (f"Видеокарта: {self.name}\n"
                f"Память: {self.memory} ГБ {self.memory_type}\n"
                f"Частота: {self.base_clock} - {self.boost_clock} МГц")

    def is_modern(self) -> bool:
        modern_memory_types = ["GDDR6", "GDDR6X", "GDDR5"]
        return self.memory_type in modern_memory_types

    def get_performance_index(self) -> int:
        return self.memory * self.boost_clock

gpu1 = GraphicsCard(
    name="RTX 4080",
    memory=16,
    memory_type="GDDR6X",
    base_clock=2205,
    boost_clock=2505
)

gpu2 = GraphicsCard(
    name="RX 6800",
    memory=16,
    memory_type="GDDR6",
    base_clock=2105,
    boost_clock=2491
)

gpu3 = GraphicsCard(
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

print(gpu3)
print(f"Актуальная: {gpu3.is_modern()}")
print(f"Индекс производительности: {gpu3.get_performance_index()}")
