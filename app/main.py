from __future__ import annotations
from math import sqrt, degrees, radians, acos, cos, sin


class Vector:

    def __init__(self, abscissa: int | float, ordinate: int | float) -> None:
        self.x = round(abscissa, 2)
        self.y = round(ordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> int | float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(other * self.x, other * self.y)

    @staticmethod
    def create_vector_by_two_points(
            start_point: tuple, end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        return round(
            degrees(
                acos(
                    (self * other) / (self.get_length() * other.get_length())
                )
            )
        )

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: int | float) -> Vector:
        return Vector(
            cos(radians(angle)) * self.x - sin(radians(angle)) * self.y,
            sin(radians(angle)) * self.x + cos(radians(angle)) * self.y
        )
