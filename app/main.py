from __future__ import annotations
from math import sqrt, degrees, acos, radians, cos, sin


class Vector:
    def __init__(self, x_value: int | float, y_value: int | float) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: Vector) -> Vector:
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other: Vector) -> Vector:
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[int | float, int | float],
            end_point: tuple[int | float, int | float]
    ) -> Vector:
        x1, y1 = start_point
        x2, y2 = end_point
        return cls(x2 - x1, y2 - y1)

    def get_length(self) -> float:
        return sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        len1 = self.get_length()
        len2 = other.get_length()
        cos_a = (self * other) / (len1 * len2)
        cos_a = max(-1.0, min(1.0, cos_a))
        angle_deg = degrees(acos(cos_a))
        return round(angle_deg)

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, deg: int) -> Vector:
        theta = radians(deg)
        x_new = self.x * cos(theta) - self.y * sin(theta)
        y_new = self.x * sin(theta) + self.y * cos(theta)
        return Vector(x_new, y_new)
