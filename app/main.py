# noqa: VNE001
from __future__ import annotations
from math import sqrt, acos, degrees, radians, cos, sin
from typing import Tuple, Union

Number = Union[int, float]


class Vector:
    def __init__(self, coor_x: Number, coor_y: Number) -> None:
        self.x = round(float(coor_x), 2)
        self.y = round(float(coor_y), 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * float(other), self.y * float(other))

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: Tuple[Number, Number],
        end_point: Tuple[Number, Number],
    ) -> "Vector":
        x1, y1 = start_point
        x2, y2 = end_point
        return cls(x2 - x1, y2 - y1)

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot = self.x * other.x + self.y * other.y
        len1 = self.get_length()
        len2 = other.get_length()

        if len1 == 0 or len2 == 0:
            return 0

        cos_value = dot / (len1 * len2)
        cos_value = max(min(cos_value, 1.0), -1.0)

        angle_deg = degrees(acos(cos_value))
        return round(angle_deg)

    def get_angle(self) -> int:
        axis_y = Vector(0, 1)
        return self.angle_between(axis_y)

    def rotate(self, deg: int) -> "Vector":
        rad = radians(deg)
        new_x = self.x * cos(rad) - self.y * sin(rad)
        new_y = self.x * sin(rad) + self.y * cos(rad)
        return Vector(new_x, new_y)
