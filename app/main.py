from __future__ import annotations
import math
from typing import Union


class Vector:

    def __init__(self, x: int | float, y: int | float) -> None:  # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
            self,
            other: Union[Vector, int, float]
    ) -> Union[Vector, int, float]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

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
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        return round(
            math.degrees(
                math.acos((self * other)
                          / (self.get_length()
                             * other.get_length()))))

    def get_angle(self) -> int:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, angle: float) -> Vector:
        return Vector(
            math.cos(
                math.radians(angle))
            * self.x - math.sin(math.radians(angle)) * self.y,
            math.sin(math.radians(angle))
            * self.x + math.cos(math.radians(angle)) * self.y
        )
