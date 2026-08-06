from __future__ import annotations
from typing import Union

from math import degrees, acos, cos, sin, radians


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[float, Vector]):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        return cls.__sub__(Vector(*end_point), Vector(*start_point))

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        lenght = self.get_length()
        self.x = round(self.x / lenght, 2)
        self.y = round(self.y / lenght, 2)
        return self

    def angle_between(self, other):
        some_angle = (self * other) / (self.get_length() * other.get_length())
        return round(degrees(acos(some_angle)))

    def get_angle(self):
        vc = Vector(0, 1)
        some_angle = (self * vc) / (self.get_length() * vc.get_length())
        return round(degrees(acos(some_angle)))

    def rotate(self, degreeses: int):
        radian = radians(degreeses)
        return Vector(cos(radian) * self.x - sin(radian) * self.y,
                      sin(radian) * self.x + cos(radian) * self.y)
