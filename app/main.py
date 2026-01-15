from __future__ import annotations
import math
from typing import Tuple


class Vector:

    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: Tuple,
                                    end_point: Tuple
                                    ) -> Vector:
        x_start, y_start = start_point
        x_end, y_end = end_point
        return cls(x_end - x_start, y_end - y_start)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        len_vector = self.get_length()
        if len_vector == 0:
            return Vector(0, 0)
        return Vector(self.x / len_vector, self.y / len_vector)

    def angle_between(self, other: Vector) -> int | float:
        if not isinstance(other, Vector):
            return 0

        len_self = self.get_length()
        len_other = other.get_length()

        if len_self == 0 or len_other == 0:
            return 0

        cos_angle = (self * other) / (len_self * len_other)
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int | float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int | float) -> Vector:
        alfa_rad = math.radians(degrees)
        rotated_x = self.x * math.cos(alfa_rad) - self.y * math.sin(alfa_rad)
        rotated_y = self.x * math.sin(alfa_rad) + self.y * math.cos(alfa_rad)
        return Vector(rotated_x, rotated_y)
