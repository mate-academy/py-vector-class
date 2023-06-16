from __future__ import annotations

import math
from typing import Union


class Vector:
    def __init__(
            self,
            coordinate_x: Union[int, float],
            coordinate_y: Union[int, float]
    ) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Union[Vector, int, float]) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
            self,
            other: Union[Vector, int, float]
    ) -> Union[Vector, int, float]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: Union[list],
            end_point: Union[list]
    ) -> Vector:
        coordinate_x = end_point[0] - start_point[0]
        coordinate_y = end_point[1] - start_point[1]
        return cls(coordinate_x, coordinate_y)

    def get_length(self) -> Union[int, float]:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Union[Vector]:
        length = self.get_length()
        if length != 0:
            return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> Union[int, float]:
        dot_product = self * other
        cos_a = dot_product / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> Union[int, float]:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        coordinate_x = self.x * cos_a - self.y * sin_a
        coordinate_y = self.x * sin_a + self.y * cos_a
        return Vector(coordinate_x, coordinate_y)
