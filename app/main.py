from __future__ import annotations
from typing import Union
import math


class Vector:
    def __init__(self, x_point: float, y_point: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
            self, other: Union[float, int, Vector]
    ) -> Union[float, Vector]:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / Vector.get_length(self), self.y / Vector.get_length(self)
        )

    def angle_between(self, other: Vector) -> int:
        dot_product = (self.x * other.x) + (self.y * other.y)
        mult_length = Vector.get_length(self) * Vector.get_length(other)
        cos_angle = dot_product / mult_length
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        return self.angle_between(
            Vector(0, abs(self.y))
        )

    def rotate(self, degrees: int) -> Vector:
        rad = math.radians(degrees)
        return Vector(
            (math.cos(rad) * self.x) - (math.sin(rad) * self.y),
            (math.sin(rad) * self.x) + (math.cos(rad) * self.y),
        )
