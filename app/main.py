# flake8: noqa: E203
from __future__ import annotations

import math
from typing import Union
from math import sqrt, degrees, acos


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
            self, other: Union[Vector, int, float]
    ) -> Union[Vector, float]:
        if not isinstance(other, Vector):
            return Vector(self.x * other, self.y * other)
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[int, int],
            end_point: tuple[int, int]
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return self * (1 / self.get_length())

    def angle_between(self, other: Vector) -> int:
        vect_mult = self * other
        vect_module = self.get_length() * other.get_length()
        cos_a = vect_mult / vect_module
        return round(degrees(acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 5))

    # x = vector[0] * math. cos(angle) - vector[1] * math. sin(angle)
    # y = vector[0] * math. sin(angle) + vector[1] * math. cos(angle)
    def rotate(self, degrees_rad: int) -> Vector:
        angle = math.radians(degrees_rad)
        new_x = self.x * math.cos(angle) - self.y * math.sin(angle)
        new_y = self.x * math.sin(angle) + self.y * math.cos(angle)
        return Vector(new_x, new_y)
