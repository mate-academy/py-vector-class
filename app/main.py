import math
from typing import Tuple, Union, Optional


class Vector:
    def __init__(
        self,
        x: float,
        y: float,
        z: Optional[float] = None,
        precision: int = 2
    ) -> None:
        self.x = round(x, precision)
        self.y = round(y, precision)
        self.z = round(z, precision) if z is not None else None
        self._precision = precision

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z if self.z is not None and other.z is not None else None,
            self._precision
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z if self.z is not None and other.z is not None else None,
            self._precision
        )

    def __mul__(
        self,
        other: Union["Vector", float, int]
    ) -> Union["Vector", float]:
        if isinstance(other, (int, float)):
            return Vector(
                self.x * other,
                self.y * other,
                self.z * other if self.z is not None else None,
                self._precision
            )
        if isinstance(other, Vector):
            dot = self.x * other.x + self.y * other.y
            if self.z is not None and other.z is not None:
                dot += self.z * other.z
            return round(dot, 4)
        return NotImplemented

    def __rmul__(self, other: Union[float, int]) -> "Vector":
        return self.__mul__(other)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return (
            math.isclose(self.x, other.x, abs_tol=10 ** -self._precision)
            and math.isclose(self.y, other.y, abs_tol=10 ** -self._precision)
            and (
                self.z is None and other.z is None
                or self.z is not None and other.z is not None
                and math.isclose(self.z, other.z, abs_tol=10 ** -self._precision)
            )
        )

    def get_length(self) -> float:
        components = [self.x, self.y]
        if self.z is not None:
            components.append(self.z)
        return round(math.sqrt(sum(c ** 2 for c in components)), self._precision)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0, 0 if self.z is not None else None, self._precision)
        return Vector(
            self.x / length,
            self.y / length,
            self.z / length if self.z is not None else None,
            self._precision
        )

    def __repr__(self) -> str:
        if self.z is not None:
            return f"Vector(x={self.x}, y={self.y}, z={self.z})"
        return
