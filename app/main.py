from __future__ import annotations
from typing import Tuple
import math


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:  # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __repr__(self) -> str:
        return f"(x: {self.x}, y: {self.y})"

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            x = self.x + other.x  # noqa: VNE001
            y = self.y + other.y  # noqa: VNE001
            return Vector(x, y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            x = self.x - other.x  # noqa: VNE001
            y = self.y - other.y  # noqa: VNE001
            return Vector(x, y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            x = self.x * other.x  # noqa: VNE001
            y = self.y * other.y  # noqa: VNE001
            return x + y

        x = round(self.x * other, 2)  # noqa: VNE001
        y = round(self.y * other, 2)  # noqa: VNE001
        return Vector(x, y)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: Tuple[int, int], end_point: Tuple[int, int]
    ) -> Vector:
        x = end_point[0] - start_point[0]  # noqa: VNE001
        y = end_point[1] - start_point[1]  # noqa: VNE001

        return Vector(x, y)

    def get_length(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> Vector:
        vector_len = self.get_length()
        x = self.x / vector_len  # noqa: VNE001
        y = self.y / vector_len  # noqa: VNE001
        return Vector(x, y)

    def dot(self, other: Vector) -> float:
        return self.x * other.x + self.y * other.y

    def angle_between(self, other: Vector) -> float:
        dot_product = self.dot(other)
        lengths = self.get_length() * other.get_length()
        cos_theta = dot_product / lengths
        return round(math.degrees(math.acos(cos_theta)))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, rotation: int) -> Vector:
        rad_rotation = math.radians(rotation)
        new_x = self.x * math.cos(rad_rotation) - self.y * math.sin(
            rad_rotation
        )  # noqa: VNE001
        new_y = self.x * math.sin(rad_rotation) + self.y * math.cos(
            rad_rotation
        )  # noqa: VNE001

        return Vector(new_x, new_y)
