from __future__ import annotations
import math
from math import radians


class Vector:
    def __init__(self, px: float, py: float) -> None:
        self.x = round(px, 2)
        self.y = round(py, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: (float, float),
                                    end_point: (float, float)) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        return round(math.degrees(math.acos(
            (self * other) / (self.get_length() * other.get_length()))))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degree: int) -> Vector:
        radian = radians(degree)
        px = self.x * math.cos(radian) - self.y * math.sin(radian)
        py = self.x * math.sin(radian) + self.y * math.cos(radian)
        return Vector(px, py)
