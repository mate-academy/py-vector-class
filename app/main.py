from __future__ import annotations
from math import sqrt, acos, degrees, cos, sin, radians, atan2


class Vector:
    def __init__(self, x: float, y: float) -> None:  # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.__class__(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls,
                                    startpoint: tuple[float, float],
                                    endpoint: tuple[float, float]) -> Vector:
        return cls(endpoint[0] - startpoint[0], endpoint[1] - startpoint[1])

    def get_length(self) -> float:
        return sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return self.__class__(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> float:
        if not isinstance(other, Vector):
            raise TypeError("Опонент має бути об'єктом Vector")

        length_prod = (self.get_length() * other.get_length())
        cos_alpha = max(-1.0, min(1.0, self * other / length_prod))
        return round(abs(degrees(acos(cos_alpha))))

    def get_angle(self) -> float:
        return round(abs(degrees(atan2(self.x, self.y))))

    def rotate(self, _degrees: int) -> Vector:
        new_x = (self.x * cos(radians(_degrees))
                 - self.y * sin(radians(_degrees)))
        new_y = (self.x * sin(radians(_degrees))
                 + self.y * cos(radians(_degrees)))
        return self.__class__(new_x, new_y)
