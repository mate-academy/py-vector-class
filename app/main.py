import math
from typing import Tuple, Union


class Vector:
    def __init__(self, x: float, y: float, precision: int = 2) -> None:
        self.x = round(x, precision)
        self.y = round(y, precision)
        self._precision = precision

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y, self._precision)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y, self._precision)

    def __mul__(self, other: Union["Vector", float, int]) -> Union["Vector", float]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self._precision)
        elif isinstance(other, Vector):
            return round(self.x * other.x + self.y * other.y, 4)
        return NotImplemented

    def __rmul__(self, other: Union[float, int]) -> "Vector":
        return self.__mul__(other)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return math.isclose(self.x, other.x, abs_tol=10**-self._precision) and \
               math.isclose(self.y, other.y, abs_tol=10**-self._precision)

    @classmethod
    def create_vector_by_two_points(
        cls, start: Tuple[float, float], end: Tuple[float, float], precision: int = 2
    ) -> "Vector":
        return cls(end[0] - start[0], end[1] - start[1], precision)

    def get_length(self) -> float:
        return round(math.hypot(self.x, self.y), self._precision)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0, self._precision)
        return Vector(self.x / length, self.y / length, self._precision)

    def angle_between(self, other: "Vector") -> int:
        dot = self * other
        len_product = self.get_length() * other.get_length()
        if len_product == 0:
            return 0
        cos_a = max(-1, min(1, dot / len_product))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self, axis: str = "y") -> int:
        length = self.get_length()
        if length == 0:
            return 0
        if axis == "y":
            cos_a = self.y / length
        elif axis == "x":
            cos_a = self.x / length
        else:
            raise ValueError("Axis must be 'x' or 'y'")
        cos_a = max(-1, min(1, cos_a))
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> "Vector":
        rad = math.radians(degrees)
        new_x = self.x * math.cos(rad) - self.y * math.sin(rad)
        new_y = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector(new_x, new_y, self._precision)

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"
