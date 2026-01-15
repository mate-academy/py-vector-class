# flake8: noqa:VNE001
from __future__ import annotations
from math import acos, degrees, sqrt, radians, cos, sin


class Vector:
    def __init__(self, x: float | int, y: float | int) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x=self.x - other.x, y=self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float | int:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(x=self.x * other, y=self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point) -> Vector:
        return cls(x=end_point[0] - start_point[0], y=end_point[1] - start_point[1])

    def get_length(self) -> float | int:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(x=self.x / self.get_length(), y=self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        self_length = self.get_length()
        other_length = other.get_length()
        cos_angle = dot_product / (self_length * other_length)
        angle_in_radians = acos(cos_angle)
        angle_in_degrees = degrees(angle_in_radians)
        return int(round(angle_in_degrees))

    def get_angle(self) -> float:
        y_axis = Vector(0, 1)
        dot_product = self * y_axis
        self_magnitude = sqrt(self.x**2 + self.y**2)
        y_axis_magnitude = sqrt(y_axis.x**2 + y_axis.y**2)
        cos_a = dot_product / (self_magnitude * y_axis_magnitude)
        angle_rad = acos(cos_a)
        angle_deg = degrees(angle_rad)
        return round(angle_deg)

    def rotate(self, degrees: int | float) -> Vector:
        radian = radians(degrees)
        new_x = self.x * cos(radian) - self.y * sin(radian)
        new_y = self.x * sin(radian) + self.y * cos(radian)
        return Vector(new_x, new_y)
