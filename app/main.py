from __future__ import annotations
from typing import Tuple

import math


class Vector:
    def __init__(self, x_cord: int | float, y_cord: int | float) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: Vector | float | int) -> float | Vector:
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)

        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: Tuple[int, int],
            end_point: Tuple[int, int]
    ) -> Vector:
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]

        return cls(new_x, new_y)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** .5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        normal_x = self.x / length
        normal_y = self.y / length

        return Vector(normal_x, normal_y)

    def angle_between(self, other: Vector) -> int:
        mul = self * other
        abs_1 = self.get_length()
        abs_2 = other.get_length()

        cos_a = mul / (abs_1 * abs_2)
        angle = math.degrees(math.acos(cos_a))

        return round(angle)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)

        rotated_x = self.x * cos_a - self.y * sin_a
        rotated_y = self.x * sin_a + self.y * cos_a

        return Vector(rotated_x, rotated_y)
