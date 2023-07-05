from __future__ import annotations
from typing import Any
import math


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: float | int | Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector((self.x + other.x), (self.y + other.y))
        return Vector((self.x + other), (self.y + other))

    def __sub__(self, other: float | int | Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector((self.x - other.x), (self.y - other.y))
        return Vector((self.x - other), (self.y - other))

    def __mul__(self, other: float | int | Vector) -> Any:
        if isinstance(other, (float, int)):
            return Vector(round((self.x * other), 2),
                          round((self.y * other), 2))
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        if isinstance(start_point, tuple) and isinstance(end_point, tuple):
            return cls(end_point[0] - start_point[0],
                       end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            round(self.x / Vector.get_length(self), 2),
            round(self.y / Vector.get_length(self), 2)
        )

    def angle_between(self, other: float | int | Vector) -> int:
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            magnitude_product = abs(
                math.sqrt(self.x ** 2 + self.y ** 2)
            ) * abs(math.sqrt(other.x ** 2 + other.y ** 2))
            return round(math.degrees(
                math.acos(dot_product / magnitude_product)))

    def get_angle(self) -> int:
        return round(abs(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        degrees = math.radians(degrees)
        rotated_x = self.x * math.cos(degrees) - self.y * math.sin(degrees)
        rotated_y = self.x * math.sin(degrees) + self.y * math.cos(degrees)
        return Vector(rotated_x, rotated_y)
