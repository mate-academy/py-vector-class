from __future__ import annotations
from typing import Union
from math import atan2, degrees, acos, cos, sin, radians


class Vector:

    def __init__(self, x_var: int | float, y_var: int | float) -> None:
        self.x = round(x_var, 2)
        self.y = round(y_var, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            round(self.x + other.x, 2),
            round(self.y + other.y, 2)
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            round(self.x - other.x, 2),
            round(self.y - other.y, 2)
        )

    def __mul__(self, other: OtherInputType) -> OtherInputType:
        if isinstance(other, (int, float)):
            return Vector(
                round(self.x * other, 2),
                round(self.y * other, 2)
            )
        else:
            return (self.x * other.x) + (self.y * other.y)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        return abs(round(
            degrees(acos((self * other)
                         / (self.get_length() * other.get_length())))
        ))

    def get_angle(self) -> int:
        return abs(round(degrees(atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        degrees = radians(degrees)
        return Vector(
            self.x * cos(degrees) - self.y * sin(degrees),
            self.x * sin(degrees) + self.y * cos(degrees)
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[int | float],
            end_point: tuple[int | float]
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )


OtherInputType = Union[Vector, int, float]
