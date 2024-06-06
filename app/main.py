from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other: Vector) -> Vector:
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector) is True:
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        start_x, start_y = start_point
        start_vector = Vector(start_x, start_y)

        end_x, end_y = end_point
        end_vector = Vector(end_x, end_y)

        return end_vector - start_vector

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        x = self.x / length
        y = self.y / length
        return Vector(x, y)

    def angle_between(self, other: Vector) -> int:
        cos_a = self * other / (self.get_length() * other.get_length())
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self) -> int:
        other = Vector(0, 1)
        return self.angle_between(other)

    def rotate(self, degrees: int) -> Vector:
        """rx = x cos α - y sin α  ry = y cos α + x sin α"""
        radians = math.radians(degrees)
        x = self.x * math.cos(radians) - self.y * math.sin(radians)
        y = self.y * math.cos(radians) + self.x * math.sin(radians)
        return Vector(x, y)
