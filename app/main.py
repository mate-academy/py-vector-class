from __future__ import annotations

import math


class Vector:

    def __init__(self, x_coor: float, y_coor: float) -> None:
        self.x = round(x_coor, 2)
        self.y = round(y_coor, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> Vector:
        x1, y1 = start_point
        x2, y2 = end_point
        new_x = x2 - x1
        new_y = y2 - y1
        return cls(new_x, new_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        cos_a = dot_product / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_val = math.cos(radians)
        sin_val = math.sin(radians)
        new_x = self.x * cos_val - self.y * sin_val
        new_y = self.x * sin_val + self.y * cos_val
        return Vector(new_x, new_y)
