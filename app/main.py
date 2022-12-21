from __future__ import annotations
from typing import Union
from math import cos, sin, radians
import math


class Vector:
    def __init__(self, cord_1: float, cord_2: float) -> None:
        self.x = round(cord_1, 2)
        self.y = round(cord_2, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: Union[int, float, Vector]) -> \
            Union[float, int, Vector]:

        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector((self.x * other), (self.y * other))

    @classmethod
    def create_vector_by_two_points(cls, v_1: tuple, v_2: tuple) -> Vector:
        return cls(-(v_1[0] - v_2[0]), -(v_1[1] - v_2[1]))

    def get_length(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def angle_between(self, other: Vector) -> float:

        product = (self.x * other.x) + (self.y * other.y)
        modul_1 = ((self.x * self.x) + (self.y * self.y)) ** 0.5
        modul_2 = ((other.x * other.x) + (other.y * other.y)) ** 0.5

        cos_a = product / (modul_1 * modul_2)

        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        vector = Vector(x=0, y=10)
        return self.angle_between(vector)

    def rotate(self, alpha: int) -> Vector:
        alpha = radians(alpha)
        x2 = (cos(alpha) * self.x) - (sin(alpha) * self.y)
        y2 = (sin(alpha) * self.x) + (cos(alpha) * self.y)
        return Vector(x2, y2)

    def get_normalized(self) -> Vector:
        lenth = self.get_length()
        inv = 1 / lenth
        return Vector((self.x * inv), (self.y * inv))
