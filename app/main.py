from __future__ import annotations
from math import sqrt, sin, cos, acos, pi


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector) -> float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    def get_length(self) -> float:
        return sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other: Vector) -> float:
        radian = 180 / pi
        return round(
            radian * acos(
                (self * other) / (self.get_length() * other.get_length())
            )
        )

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = degrees * pi / 180
        return Vector(
            round(self.x * cos(radians) - self.y * sin(radians), 2),
            round(self.x * sin(radians) + self.y * cos(radians), 2),
        )

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_p: tuple,
                                    end_p: tuple) -> Vector:

        return Vector(end_p[0] - start_p[0], end_p[1] - start_p[1])
