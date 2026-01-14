from __future__ import annotations
from typing import Union
from math import degrees, acos, cos, sin, radians


class Vector:
    def __init__(self, x_cr: float, y_cr: float) -> None:
        self.x = round(x_cr, 2)
        self.y = round(y_cr, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[Vector, int, float]) \
            -> Union[Vector, float]:
        if not isinstance(other, Vector):
            return Vector(self.x * other, self.y * other)
        else:
            dot_product = (self.x * other.x) + (self.y * other.y)
            return dot_product

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        x_cr = end_point[0] - start_point[0]
        y_cr = end_point[1] - start_point[1]
        return cls(x_cr, y_cr)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        x_cr = round(self.x / self.get_length(), 2)
        y_cr = round(self.y / self.get_length(), 2)
        return Vector(x_cr, y_cr)

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        cos_a = dot_product / (self.get_length() * other.get_length())
        return round(degrees(acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = (self.x * 0 + self.y * ((self.y ** 2) ** 0.5)) / \
                (self.get_length() * Vector(0, self.y).get_length())
        return round(degrees(acos(cos_a)))

    def rotate(self, angle: int) -> Vector:
        x_cr = (cos(radians(angle)) * self.x) - (sin(radians(angle)) * self.y)
        y_cr = (sin(radians(angle)) * self.x) + (cos(radians(angle)) * self.y)
        return Vector(x_cr, y_cr)
