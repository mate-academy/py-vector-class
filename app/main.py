from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()
        return Vector(self.x / vector_length, self.y / vector_length)

    def angle_between(self, other: Vector) -> int:
        cos = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        cos_degrees = math.cos(math.radians(degrees))
        sin_degrees = math.sin(math.radians(degrees))
        rotated_x = self.x * cos_degrees - self.y * sin_degrees
        rotated_y = self.x * sin_degrees + self.y * cos_degrees
        return Vector(rotated_x, rotated_y)
