from abc import ABC, abstractmethod


class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None

    def __str__(self):
        return f"Computer(cpu={self.cpu}, ram={self.ram}, storage={self.storage})"


class ComputerBuilder(ABC):

    @abstractmethod
    def set_cpu(self):
        pass

    @abstractmethod
    def set_ram(self):
        pass

    @abstractmethod
    def set_storage(self):
        pass

    @abstractmethod
    def get_result(self) -> Computer:
        pass


class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self):
        self.computer.cpu = "Intel Core i9"

    def set_ram(self):
        self.computer.ram = "32 GB"

    def set_storage(self):
        self.computer.storage = "1 TB SSD"

    def get_result(self) -> Computer:
        return self.computer


class Director:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder

    def build_computer(self) -> Computer:
        self.builder.set_cpu()
        self.builder.set_ram()
        self.builder.set_storage()
        return self.builder.get_result()


if __name__ == "__main__":
    builder = GamingComputerBuilder()
    director = Director(builder)

    computer = director.build_computer()
    print(computer)
