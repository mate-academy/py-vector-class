from __future__ import annotations
from typing import Self
import math


class Vector:
    def __init__(self, x_axis: int | float, y_axis: int | float) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x_axis=self.x + other.x, y_axis=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x_axis=self.x - other.x, y_axis=self.y - other.y)

    def __mul__(self, other: Vector) -> Vector | int | float:
        if isinstance(other, (int, float)):
            return Vector(x_axis=self.x * other, y_axis=self.y * other)
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: int | float,
            end_point: int | float
    ) -> Self:
        return cls(
            x_axis=end_point[0] - start_point[0],
            y_axis=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(x_axis=(self.x / length), y_axis=self.y / length)

    def angle_between(self, other: Vector) -> int:
        numerator = self.x * other.x + self.y * other.y
        consequent = self.get_length() * other.get_length()
        cos = numerator / consequent
        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> int:
        numerator = self.y
        consequent = self.get_length()
        cos = numerator / consequent
        return round(math.degrees(math.acos(cos)))

    def rotate(self, degrees: int | float) -> Vector:
        cos = math.cos(math.radians(degrees))
        sin = math.sin(math.radians(degrees))
        return Vector(
            x_axis=self.x * cos - self.y * sin,
            y_axis=self.x * sin + self.y * cos
        )
