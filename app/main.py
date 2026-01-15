from __future__ import annotations

import math
from typing import Union, Tuple


class Vector:

    def __init__(self, x_cord: float, y_cord: float) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other: Vector) -> Union[Vector, float]:
        if isinstance(other, (int, float)):
            new_x = self.x * other
            new_y = self.y * other
            return Vector(new_x, new_y)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: Tuple,
                                    end_point: Tuple) -> Vector:
        start_x, start_y = start_point
        end_x, end_y = end_point
        vector_x = end_x - start_x
        vector_y = end_y - start_y
        return cls(vector_x, vector_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        normalized_x = self.x / length
        normalized_y = self.y / length
        return Vector(normalized_x, normalized_y)

    def angle_between(self, other: Vector) -> float:
        dot_product = self * other
        length_self = self.get_length()
        length_other = other.get_length()

        if length_self == 0 or length_other == 0:
            return 0

        cos_angle = dot_product / (length_self * length_other)
        cos_angle = max(-1.0, min(1.0, cos_angle))

        angle_rad = math.acos(cos_angle)
        angle_deg = math.degrees(angle_rad)

        return round(angle_deg, 0)

    def get_angle(self) -> float:
        y_axis = Vector(0, 1)
        angle = self.angle_between(y_axis)
        return angle

    def rotate(self, degrees: int) -> Vector:

        radians = math.radians(degrees)

        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)

        new_x = self.x * cos_angle - self.y * sin_angle
        new_y = self.x * sin_angle + self.y * cos_angle

        return Vector(new_x, new_y)
