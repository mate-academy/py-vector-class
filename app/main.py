from __future__ import annotations
import math


class Vector:
    def __init__(self, first: float, second: float) -> None:
        self.x = round(first, 2)
        self.y = round(second, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, float | int):
            return Vector((self.x * other), (self.y * other))
        elif isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        first = end[0] - start[0]
        second = end[1] - start[1]
        return Vector(first, second)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        long = self.get_length()
        return Vector(self.x / long, self.y / long)

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        other = Vector(0, 1)
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)

        new_x = self.x * cos_angle - self.y * sin_angle
        new_y = self.x * sin_angle + self.y * cos_angle

        return Vector(new_x, new_y)
