import abc


class Parrot(abc.ABC):
    @staticmethod
    def _base_speed() -> float:
        return 12.0

    @abc.abstractmethod
    def speed(self) -> float:
        ...

    @abc.abstractmethod
    def cry(self) -> str:
        ...


class NorwegianParrot(Parrot):
    def __init__(self, voltage: float, nailed: bool):
        self._voltage = voltage
        self._nailed = nailed

    def cry(self) -> str:
        if self._voltage > 0:
            return "Bzzzzzz"
        else:
            return "..."

    def speed(self) -> float:
        if self._nailed:
            return 0
        else:
            return min(24.0, self._voltage * self._base_speed())


class EuropeanParrot(Parrot):
    def cry(self) -> str:
        return "Sqoork!"

    def speed(self) -> float:
        return self._base_speed()


class AfricanParrot(Parrot):
    def __init__(self, number_of_coconuts: float):
        self._number_of_coconuts = number_of_coconuts

    def cry(self) -> str:
        return "Sqaark!"

    @staticmethod
    def _load_factor() -> float:
        return 9.0

    def speed(self) -> float:
        return max(
            0.0,
            self._base_speed() - self._load_factor() * self._number_of_coconuts,
        )
