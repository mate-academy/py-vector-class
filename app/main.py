from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> Vector:
        x1, y1 = start_point
        x2, y2 = end_point
        return cls(x2 - x1, y2 - y1)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ValueError("Error: division by 0")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot = self * other
        len_self = self.get_length()
        len_other = other.get_length()
        cos_a = dot / (len_self * len_other)
        angle_deg = math.degrees(math.acos(cos_a))
        return round(angle_deg)

    def get_angle(self) -> int:
        dot = self * Vector(0.0, 1.0)
        len_self = self.get_length()
        if len_self == 0:
            raise ValueError("Error: zero-length vector")
        cos_a = dot / len_self
        angle_deg = math.degrees(math.acos(cos_a))
        return round(angle_deg)

    def rotate(self, degrees: int) -> Vector:
        rad = math.radians(degrees)
        cos_r = math.cos(rad)
        sin_r = math.sin(rad)
        x_new = self.x * cos_r - self.y * sin_r
        y_new = self.x * sin_r + self.y * cos_r
        return Vector(x_new, y_new)
