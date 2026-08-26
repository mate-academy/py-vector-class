from __future__ import annotations
import math


class Vector:
    def __init__(self, xx: float | int, yy: float | int) -> None:
        self.x = round(xx, 2)
        self.y = round(yy, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return Vector(end[0] - start[0], end[1] - start[1])

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int | float:
        dot_product = self.x * other.x + self.y * other.y
        length1 = self.get_length()
        length2 = other.get_length()
        cos_angle = dot_product / (length1 * length2)
        cos_angle = min(1, max(-1, cos_angle))
        angle_radians = math.acos(cos_angle)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def get_angle(self) -> int:
        angle_radians = math.atan2(-self.x, self.y)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees % 360)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(new_x, 2), round(new_y, 2))
