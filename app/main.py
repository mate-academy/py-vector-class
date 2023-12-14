from __future__ import annotations

import math


class Vector:
    def __init__(self, x: float, y: float) -> Vector:
        self.x = round(x, 2)
        self.y = round(y, 2)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> Vector:
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(
            x=self.x / length,
            y=self.y / length
        )

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        angle = math.degrees(math.acos(
            dot_product / (self.get_length() * other.get_length())
        ))
        return round(angle)

    def get_angle(self) -> int:
        angle = math.degrees(math.acos(self.y / self.get_length()))
        return round(angle)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(
            x=math.cos(radians) * self.x - math.sin(radians) * self.y,
            y=math.sin(radians) * self.x + math.cos(radians) * self.y
        )

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            x=self.x * other,
            y=self.y * other
        )
