from __future__ import annotations

import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            first_point: tuple,
            second_point: tuple
    ) -> Vector:
        return cls(
            second_point[0] - first_point[0],
            second_point[1] - first_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        dot_product = self * other
        len_product = self.get_length() * other.get_length()

        if len_product == 0:
            raise ValueError("Can't compute angle with zero-length vector")
        cos_a = max(-1.0, min(1.0, dot_product / len_product))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        in_radians = math.radians(degrees)
        cos_a = math.cos(in_radians)
        sin_a = math.sin(in_radians)

        return Vector(
            self.x * cos_a - self.y * sin_a,
            self.x * sin_a + self.y * cos_a
        )
