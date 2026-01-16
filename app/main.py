from __future__ import annotations
import math
from math import acos, cos, radians, sin


class Vector:
    def __init__(
            self,
            x_axis: int | float,
            y_axis: int | float
    ) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if not isinstance(other, (Vector, int, float)):
            raise TypeError("Argument must be 'int' or 'Vector' type!")
        elif isinstance(other, int | float):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        else:
            return other.x * self.x + other.y * self.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            x_axis=end_point[0] - start_point[0],
            y_axis=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()
        return Vector(
            round(self.x / vector_length, 2),
            round(self.y / vector_length, 2)
        )

    def angle_between(self, other: Vector) -> int:
        return round(
            math.degrees(
                acos(self * other / (self.get_length() * other.get_length()))
            )
        )

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, abs(self.y)))

    def rotate(self, angle: int) -> Vector:
        rads = radians(angle)
        return Vector(
            cos(rads) * self.x - sin(rads) * self.y,
            sin(rads) * self.x + cos(rads) * self.y
        )
