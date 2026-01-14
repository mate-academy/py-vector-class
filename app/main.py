from __future__ import annotations
from typing import Any
import math


class Vector:
    def __init__(self, x_variable: float, y_variable: float) -> None:
        self.x = round(x_variable, 2)
        self.y = round(y_variable, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, int | float):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> Vector:
        x_variable = end_point[0] - start_point[0]
        y_variable = end_point[1] - start_point[1]
        return cls(x_variable, y_variable)

    def get_length(self) -> float:
        return abs(math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2)))

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        magnitude_self = self.get_length()
        magnitude_other = other.get_length()
        cos_theta = dot_product / (magnitude_self * magnitude_other)
        angle_radians = math.acos(cos_theta)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def get_angle(self) -> int:
        angle_radians = math.atan2(self.x, self.y)
        angle_degrees = math.degrees(angle_radians)
        return abs(round(angle_degrees))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        x_new = self.x * cos_theta - self.y * sin_theta
        y_new = self.x * sin_theta + self.y * cos_theta
        return Vector(x_new, y_new)
