from __future__ import annotations

from math import acos, cos, sin, degrees, radians


class Vector:
    def __init__(self, first: float, second: float) -> None:
        self.x = round(first, 2)
        self.y = round(second, 2)

    def __add__(self, other: int | Vector) -> Vector:
        return Vector(
            self.x + other.x, self.y + other.y
        )

    def __sub__(self, other: int | Vector) -> Vector:
        return Vector(
            self.x - other.x, self.y - other.y
        )

    def __mul__(self, other: float | int | Vector) -> Vector | int | float:
        if type(other) in [int, float]:
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return (self.x * other.x) + (
                self.y * other.y
            )

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (
            self.x * self.x + self.y * self.y
        ) ** 0.5

    def get_normalized(self) -> Vector:
        first_coord = self.x / self.get_length()
        second_coord = self.y / self.get_length()
        return Vector(first_coord, second_coord)

    def angle_between(self, vector: Vector) -> int:
        angle = acos(
            (vector.x * self.x + vector.y * self.y)
            / (
                (self.x**2 + self.y**2) ** 0.5
                * (vector.x**2 + vector.y**2) ** 0.5
            )
        )
        return round(degrees(angle))

    def get_angle(self) -> int:
        angle = acos(
            (0 * self.x + 1 * self.y)
            / (
                (self.x**2 + self.y**2) ** 0.5
                * (0 * 0 + 1 * 1) ** 0.5
            )
        )
        return round(degrees(angle))

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            (
                self.x * cos(radians(degrees))
                - self.y * sin(radians(degrees))
            ),
            (
                self.x * sin(radians(degrees))
                + self.y * cos(radians(degrees))
            ),
        )
