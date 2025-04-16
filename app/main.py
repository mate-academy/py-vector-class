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
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        coordinate_x = self.x / self.get_length()
        coordinate_y = self.y / self.get_length()
        return Vector(coordinate_x, coordinate_y)

    def angle_between(self, other: Vector) -> float:
        cos_a = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: int) -> Vector:
        sin_y = self.y / self.get_length()
        sin_x = self.x / self.get_length()
        y = (math.sin(math.asin(sin_y) + math.radians(degrees))) * self.get_length()
        x = (math.sin(math.asin(sin_x) - math.radians(degrees))) * self.get_length()
        return Vector(x, y)