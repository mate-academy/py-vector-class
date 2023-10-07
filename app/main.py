from __future__ import annotations

import math
from math import sqrt, degrees, acos, atan2, cos, sin


class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:

        if isinstance(other, Vector):
            return Vector(
                self.x + other.x,
                self.y + other.y
            )

    def __sub__(self, other: Vector) -> Vector:

        if isinstance(other, Vector):
            return Vector(
                self.x - other.x,
                self.y - other.y
            )

    def __mul__(self, other: Vector | int | float) -> Vector | float:

        if isinstance(other, int) or isinstance(other, float):
            return Vector(
                self.x * other,
                self.y * other
            )

        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            point_one: tuple,
            point_two: tuple
    ) -> Vector:
        return Vector(
            point_two[0] - point_one[0],
            point_two[1] - point_one[1]
        )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:

        mult = self * other
        one_length = self.get_length()
        two_length = other.get_length()

        cos_a = mult / (one_length * two_length)

        degree = degrees(acos(cos_a))

        return round(degree, 0)

    def get_angle(self) -> int:
        angle_radians = atan2(self.x, self.y)
        angle_degrees = degrees(angle_radians)
        return int(angle_degrees) * (-1)

    def rotate(self, degree: int | float) -> Vector:
        radians = math.radians(degree)

        new_x = self.x * cos(radians) - self.y * sin(radians)
        new_y = self.x * sin(radians) + self.y * cos(radians)

        return Vector(new_x, new_y)
