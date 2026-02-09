# flake8: noqa: E741
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

    def __mul__(self, other: float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return cls(
            end[0] - start[0],
            end[1] - start[1],
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2),
        )

    def angle_between(self, other: Vector) -> float:
        up = self.x * other.x + self.y * other.y
        down = (math.sqrt(self.x ** 2 + self.y ** 2)
                * math.sqrt(other.x ** 2 + other.y ** 2))
        return round(math.degrees(math.acos(up / down)))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, abs(self.y)))

    def rotate(self, angle: float) -> Vector:
        cos_radians = math.cos(math.radians(angle))
        sin_radians = math.sin(math.radians(angle))
        return Vector(round(self.x * cos_radians - self.y * sin_radians, 2),
                      round(self.y * cos_radians + self.x * sin_radians, 2))
