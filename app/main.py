from __future__ import annotations

import math
from math import (
    sqrt, acos, degrees,
    radians, cos, sin,
)


class Vector:
    def __init__(self, x_point: float, y_point: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            round(self.x * other, 2),
            round(self.y * other, 2),
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a vector with length 0")

        return Vector(
            round(self.x / length, 2),
            round(self.y / length, 2),
        )

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        magnitude_self = self.get_length()
        magnitude_other = sqrt(other.x ** 2 + other.y ** 2)

        cosine_angle = dot_product / (magnitude_self * magnitude_other)
        angle_in_degrees = degrees(acos(cosine_angle))

        return round(angle_in_degrees)

    def get_angle(self) -> int:
        vector = Vector(0, abs(self.y))
        angle = self * vector / (self.get_length() * vector.get_length())
        angle_in_degree = math.degrees(math.acos(angle))

        return round(angle_in_degree)

    def rotate(self, degrees: int) -> Vector:
        angle_in_radians = radians(degrees)

        return Vector(
            self.x * cos(angle_in_radians) - self.y * sin(angle_in_radians),
            self.x * sin(angle_in_radians) + self.y * cos(angle_in_radians)
        )
