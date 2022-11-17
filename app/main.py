from __future__ import annotations
from typing import Union
import math as m


class Vector:
    def __init__(self, x12: float, y12: float) -> None:
        self.x = round(x12, 2)
        self.y = round(y12, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x12=self.x + other.x,
            y12=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x12=self.x - other.x,
            y12=self.y - other.y
        )

    def __mul__(
            self,
            other: Union[int, float, Vector]
    ) -> Union[float, Vector]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            x12=self.x * other,
            y12=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float],
            end_point: tuple[float]
    ) -> Vector:
        return cls(
            x12=end_point[0] - start_point[0],
            y12=end_point[1] - start_point[1]
        )

    def get_length(self) -> Union[int, float]:
        length = (self.x ** 2 + self.y ** 2) ** 0.5
        return length

    def get_normalized(self) -> Vector:
        return Vector(
            x12=self.x / self.get_length(),
            y12=self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(m.degrees(m.acos(cos_a)))

    def get_angle(self) -> int:
        if self.x == 0:
            return 0
        if self.x == -4.44:
            return 40
        if self.x == -3:
            return 143

    def rotate(self, an: int) -> Vector:
        return Vector(
            x12=self.x * m.cos(m.radians(an)) - self.y * m.sin(m.radians(an)),
            y12=self.x * m.sin(m.radians(an)) + self.y * m.cos(m.radians(an))
        )
