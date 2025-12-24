from __future__ import annotations
import math
from typing import Union

class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[float, Vector]) -> Union[float, Vector]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError("Unsupported type for multiplication")

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> Vector:
        x_start, y_start = start_point
        x_end, y_end = end_point
        x = x_end - x_start
        y = y_end - y_start
        return cls(x, y)

    def get_length(self) -> float:
        return round(math.sqrt(self.x ** 2 + self.y ** 2), 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        length_self = self.get_length()
        length_other = other.get_length()
        cos_theta = dot_product / (length_self * length_other)
        cos_theta = max(-1.0, min(1.0, cos_theta))
        return round(math.degrees(math.acos(cos_theta)))

    def get_angle(self) -> int:
        angle_radians = math.atan2(self.y, self.x)
        angle_deg = math.degrees(angle_radians)
        if angle_deg < 0:
            angle_deg += 360
        return round(angle_deg)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta
        return Vector(new_x, new_y)
