# flake8: noqa: VNE001

from __future__ import annotations

import math
from typing import Union


class Vector:
    def __init__(self, x: Union[int, float], y: Union[int, float]) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[
        Vector,
        int,
        float
    ]
    ) -> Union[Vector, int, float]:
        if not isinstance(other, Vector):
            return Vector(self.x * other, self.y * other)
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return cls(x=end[0] - start[0], y=end[1] - start[1])

    def get_length(self) -> Union[float, int]:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        return Vector(
            (self.x / self.get_length()),
            (self.y / self.get_length())
        )

    def angle_between(self, other: Vector) -> int:
        dot_product = self.x * other.x + self.y * other.y
        magnitudes_product = self.get_length() * other.get_length()

        cos_angle = dot_product / magnitudes_product
        angle_radians = math.acos(cos_angle)
        angle_degrees = math.degrees(angle_radians)

        return int(round(angle_degrees))

    def get_angle(self) -> int:
        angle_radians = math.atan2(self.x, self.y)
        angle_degrees = math.degrees(angle_radians)
        return abs(int(round(angle_degrees)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
