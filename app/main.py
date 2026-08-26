from __future__ import annotations
from math import acos, cos, sin, degrees, radians


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[int | float, int | float],
        end_point: tuple[int | float, int | float],
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        return round(
            degrees(
                acos(self * other / (self.get_length() * other.get_length()))
            )
        )

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        rad = radians(degrees)
        sin_ = sin(rad)
        cos_ = cos(rad)
        return Vector(
            cos_ * self.x - sin_ * self.y,
            sin_ * self.x + cos_ * self.y,
        )
