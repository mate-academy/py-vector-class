from __future__ import annotations
import math


class Vector:
    def __init__(self, vx: float, vy: float) -> None:
        self.x = round(vx, 2)
        self.y = round(vy, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: Vector | int | float) -> float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector((self.x * other), (self.y * other))

    @classmethod
    def create_vector_by_two_points(cls, start: Vector, end: Vector) -> Vector:
        return cls((end[0] - start[0]), (end[1] - start[1]))

    def get_length(self) -> float:
        return ((self.x ** 2) + (self.y ** 2)) ** (1 / 2)

    def get_normalized(self) -> Vector:
        length = 1 / self.get_length()
        return Vector((self.x * length), (self.y * length))

    def angle_between(self, other: Vector) -> int:
        skalar = (self.x * other.x) + (self.y * other.y)
        modul_self = self.get_length()
        modul_other = other.get_length()
        cos_a = skalar / (modul_self * modul_other)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int | float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        cos = math.cos(math.radians(degrees))
        sin = math.sin(math.radians(degrees))
        rotatedx = self.x * cos - self.y * sin
        rotatedy = self.x * sin + self.y * cos
        return Vector(rotatedx, rotatedy)
