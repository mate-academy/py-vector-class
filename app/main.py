from __future__ import annotations
from typing import Union, Any
import math


class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[float, Vector]) -> Union[Vector, float]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> Any:
        return cls(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        coefficient = 1 / self.get_length()
        return Vector(coefficient * self.x, coefficient * self.y)

    def angle_between(self, other: Vector) -> int:
        cos_angle = self.__mul__(other) / (self.get_length() * other.get_length())
        angle = math.degrees(math.acos(cos_angle))
        return round(angle)

    def get_angle(self) -> int:
        other = Vector(0, 1)
        cos_angle = self.__mul__(other) / (self.get_length() * other.get_length())
        angle = math.degrees(math.acos(cos_angle))
        return round(angle)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        return Vector(self.x * cos_a - self.y * sin_a, self.x * sin_a + self.y * cos_a)
