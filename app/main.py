from __future__ import annotations
from typing import Any
import math


class Vector:
    def __init__(self, x_value: float, y_value: float) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: Vector | Any) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector | Any) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int) -> float | Vector:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        inversion_length = 1 / self.get_length()
        return Vector(self.x * inversion_length, self.y * inversion_length)

    def angle_between(self, other: Vector) -> int:
        dot_product = (self.x * other.x) + (self.y * other.y)
        magnitude_of_vectors = self.get_length() * other.get_length()
        return round(
            math.degrees(math.acos(dot_product / magnitude_of_vectors))
        )

    def get_angle(self) -> int:
        positive_y_axis = Vector(0, 1)
        return self.angle_between(positive_y_axis)

    def rotate(self, degrees: int) -> Vector:
        radians_angle = math.radians(degrees)
        sin_theta = math.sin(radians_angle)
        cos_theta = math.cos(radians_angle)
        return Vector(
            (self.x * cos_theta) - (self.y * sin_theta),
            (self.x * sin_theta) + (self.y * cos_theta)
        )
