from __future__ import annotations
import math
from typing import Tuple


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            return NotImplemented
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            return NotImplemented
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other: float | int | Vector) -> Vector | float:
        if isinstance(other, (float, int)):
            new_x = self.x * other
            new_y = self.y * other
            return Vector(new_x, new_y)

        elif isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            return dot_product

        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: Tuple[float, float],
            end_point: Tuple[float, float]
    ) -> Vector:
        x_start, y_start = start_point
        x_end, y_end = end_point

        vector_x = x_end - x_start
        vector_y = y_end - y_start

        return cls(vector_x, vector_y)

    def get_length(self) -> float:
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        return length

    def get_normalized(self) -> Vector:
        length = self.get_length()

        if length == 0:
            return Vector(0, 0)

        norm_x = self.x / length
        norm_y = self.y / length

        return Vector(norm_x, norm_y)

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        len_product = self.get_length() * other.get_length()

        if len_product == 0:
            return 0

        cos_a = dot_product / len_product
        cos_a = max(min(cos_a, 1.0), -1.0)

        angle_rad = math.acos(cos_a)
        angle_deg = math.degrees(angle_rad)

        return round(angle_deg)

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        angle = self.angle_between(y_axis)
        return angle

    def rotate(self, degrees: int) -> Vector:
        angle_rad = math.radians(degrees)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)

        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a

        return Vector(new_x, new_y)
