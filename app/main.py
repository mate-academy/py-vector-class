from __future__ import annotations
import math


class Vector:
    def __init__(self, point_x: int, point_y: int | float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: int | float) -> "Vector":
        self.x = self.x + other.x
        self.y = self.y + other.y
        return Vector(self.x, self.y)

    def __sub__(self, other: int | float) -> "Vector":
        self.x = self.x - other.x
        self.y = self.y - other.y
        return Vector(self.x, self.y)

    def __mul__(self, other: int | float) -> int | float | "Vector":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> "Vector":
        pnt_x = (end[0] - start[0])
        pnt_y = (end[1] - start[1])
        return Vector(pnt_x, pnt_y)

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        norm_x = self.x / self.get_length()
        norm_y = self.y / self.get_length()
        return Vector(norm_x, norm_y)

    def angle_between(self, other: "Vector") -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, other: float | int | "Vector") -> "Vector":
        radians = math.radians(other)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        rotate_x = self.x * cos_angle - self.y * sin_angle
        rotate_y = self.x * sin_angle + self.y * cos_angle
        return Vector(rotate_x, rotate_y)
ssss