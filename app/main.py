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

    def __mul__(self, other: Vector | tuple) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2)**0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        angle = math.acos((self.x * other.x + self.y * other.y)
                          / (self.get_length() * other.get_length()))
        return round(math.degrees(angle))

    def get_angle(self) -> int:
        cos_a = (self.y / self.get_length())
        return int(math.degrees(math.acos(cos_a)))

    def rotate(self, angle: int) -> Vector:
        cos_a = math.cos(math.radians(angle))
        sin_a = math.sin(math.radians(angle))
        x1 = cos_a * self.x - sin_a * self.y
        y1 = sin_a * self.x + cos_a * self.y
        return Vector(x1, y1)
