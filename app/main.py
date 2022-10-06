from __future__ import annotations
import math


class Vector:
    def __init__(self, px: float, py: float) -> None:
        self.x = round(px, 2)
        self.y = round(py, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: object) -> object:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return Vector(end[0], end[1]) - Vector(start[0], start[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        coef_norm = self.get_length()
        return Vector(self.x / coef_norm, self.y / coef_norm)

    def angle_between(self, other: Vector) -> float:
        ab = self.x * other.x + self.y * other.y
        amod = math.fabs((self.x ** 2 + self.y ** 2) ** 0.5)
        bmod = math.fabs((other.x ** 2 + other.y ** 2) ** 0.5)
        cos_a = ab / (amod * bmod)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: float) -> Vector:
        rad = math.radians(degrees)
        x1 = self.x * math.cos(rad) - self.y * math.sin(rad)
        y1 = self.y * math.cos(rad) + self.x * math.sin(rad)
        return Vector(x1, y1)
