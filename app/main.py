from __future__ import annotations
from typing import Tuple
import math


class Vector:
    def __init__(self, new_x: int | float, new_y: int | float) -> None:
        self.x = round(new_x, 2)
        self.y = round(new_y, 2)

    def __repr__(self) -> str:
        return f"(x: {self.x}, new_y: {self.y})"

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Vector(new_x, new_y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            new_x = self.x - other.x
            new_y = self.y - other.y
            return Vector(new_x, new_y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            new_x = self.x * other.x
            new_y = self.y * other.y
            return new_x + new_y

        new_x = round(self.x * other, 2)
        new_y = round(self.y * other, 2)
        return Vector(new_x, new_y)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: Tuple[int, int], end_point: Tuple[int, int]
    ) -> Vector:
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]

        return Vector(new_x, new_y)

    def get_length(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> Vector:
        vector_len = self.get_length()
        new_x = self.x / vector_len
        new_y = self.y / vector_len
        return Vector(new_x, new_y)

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
        rad_rot = math.radians(rotation)
        new_x = self.x * math.cos(rad_rot) - self.y * math.sin(rad_rot)
        new_y = self.x * math.sin(rad_rot) + self.y * math.cos(rad_rot)

        return Vector(new_x, new_y)
