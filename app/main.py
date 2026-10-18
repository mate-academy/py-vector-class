from __future__ import annotations

from math import acos, cos, degrees, radians, sin
from typing import Self


class Vector:
    def __init__(self, x: float, y: float) -> None:  # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector) -> float | Vector:
        if isinstance(other, int | float):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Self:
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, vector: Vector) -> int:
        return round(
            degrees(
                acos(self * vector / self.get_length() / vector.get_length())
            )
        )

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            cos(radians(degrees)) * self.x - sin(radians(degrees)) * self.y,
            sin(radians(degrees)) * self.x + cos(radians(degrees)) * self.y,
        )
