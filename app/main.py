from __future__ import annotations

import math
from typing import Union, Tuple

Number = Union[int, float]


class Vector:
    def __init__(self, x_coord: Number, y_coord: Number) -> None:
        self.x = round(float(x_coord), 2)
        self.y = round(float(y_coord), 2)

    def __add__(self, other: object) -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: object) -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: object) -> Union["Vector", float]:
        if isinstance(other, (int, float)):
            factor = float(other)
            return Vector(self.x * factor, self.y * factor)

        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

        return NotImplemented

    def __rmul__(self, other: object) -> "Vector":
        if isinstance(other, (int, float)):
            factor = float(other)
            return Vector(factor * self.x, factor * self.y)
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: Tuple[Number, Number],
        end_point: Tuple[Number, Number],
    ) -> "Vector":
        start_x_coord, start_y_coord = start_point
        end_x_coord, end_y_coord = end_point
        return cls(end_x_coord - start_x_coord, end_y_coord - start_y_coord)

    def get_length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize zero-length vector.")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        length_self = self.get_length()
        length_other = other.get_length()
        if length_self == 0 or length_other == 0:
            raise ValueError("Angle is undefined for zero-length vector.")

        dot_product = self * other
        cos_value = dot_product / (length_self * length_other)
        cos_value = max(-1.0, min(1.0, cos_value))

        angle_degrees = math.degrees(math.acos(cos_value))
        return round(angle_degrees)

    def get_angle(self) -> int:
        if self.x == 0 and self.y == 0:
            raise ValueError("Angle is undefined for zero vector.")

        angle_degrees = math.degrees(math.atan2(self.x, self.y))
        if angle_degrees < 0:
            angle_degrees += 360

        return round(angle_degrees)

    def rotate(self, degrees: int) -> "Vector":
        radians_value = math.radians(degrees)
        cos_value = math.cos(radians_value)
        sin_value = math.sin(radians_value)

        new_x_coord = self.x * cos_value - self.y * sin_value
        new_y_coord = self.x * sin_value + self.y * cos_value
        return Vector(new_x_coord, new_y_coord)
