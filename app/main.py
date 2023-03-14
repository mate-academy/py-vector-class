from __future__ import annotations
from math import degrees as deg
from math import acos as ac
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )

    def __mul__(self, other: Vector | float) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            self.x * other,
            self.y * other,
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple,
    ) -> Vector:
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1],
        )

    @property
    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length_vector = self.get_length
        return Vector(
            x=round(self.x / length_vector, 2),
            y=round(self.y / length_vector, 2),
        )

    def angle_between(self, other: Vector) -> float:
        cos_a = self * other / (self.get_length * other.get_length)
        return round(deg(ac(cos_a)))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: float) -> Vector:
        a_in_r = math.radians(degrees)
        return Vector(
            x=round(self.x * math.cos(a_in_r) - self.y * math.sin(a_in_r), 2),
            y=round(self.x * math.sin(a_in_r) + self.y * math.cos(a_in_r), 2)
        )
