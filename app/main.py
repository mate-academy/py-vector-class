# flake8: noqa: VNE001

from __future__ import annotations

import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x=self.x + other.x,
                      y=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x=self.x - other.x,
                      y=self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            dot_product = ((self.x * other.x)
                           + (self.y * other.y))
            return dot_product
        if isinstance(other, float | int):
            return Vector(x=self.x * other,
                          y=self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        cls.x = end_point[0] - start_point[0]
        cls.y = end_point[1] - start_point[1]
        return Vector(cls.x, cls.y)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length_vector = (self.x ** 2
                         + self.y ** 2) ** 0.5
        return Vector(self.x / length_vector,
                      self.y / length_vector)

    def angle_between(self, other: Vector) -> int:
        cos_angle = (((self.x * other.x)
                      + (self.y * other.y))
                     / (((self.x ** 2 + self.y ** 2) ** 0.5)
                        * ((other.x ** 2) + (other.y ** 2)) ** 0.5))
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        atan_angle = math.atan2(self.x, self.y)
        return abs(round(math.degrees(atan_angle)))

    def rotate(self, degrees: int) -> Vector:
        new_x = (math.cos(math.radians(degrees)) * self.x
                 - math.sin(math.radians(degrees)) * self.y)
        new_y = (math.sin(math.radians(degrees)) * self.x
                 + math.cos(math.radians(degrees)) * self.y)
        return Vector(new_x, new_y)
