from __future__ import annotations
from typing import Any
from math import sqrt, degrees, acos, atan2, cos, sin, radians


class Vector:
    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float, float],
            end_point: tuple[float, float]
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    @staticmethod
    def raise_type_error(value: Any) -> TypeError:
        raise TypeError(f"Type of {value} ({type(value)}) is incompatible")

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize zero vector")
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: Vector) -> float:
        dot_product = self.x * other.x + self.y * other.y
        lengths = self.get_length() * other.get_length()
        cos_angle = dot_product / lengths
        return round(degrees(acos(cos_angle)))

    def get_angle(self) -> float:
        if not self.x or not self.y:
            return 0

        angle = degrees(atan2(-self.x, self.y))
        return round(angle) if angle >= 0 else round(angle + 360)

    def rotate(self, angle: float) -> Vector:
        rad = radians(angle)
        new_x = self.x * cos(rad) - self.y * sin(rad)
        new_y = self.x * sin(rad) + self.y * cos(rad)
        return Vector(round(new_x, 2), round(new_y, 2))

    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        self.raise_type_error(other)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        self.raise_type_error(other)

    def __mul__(self, other: float | Vector) -> float | Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        self.raise_type_error(other)
