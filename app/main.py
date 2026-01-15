from __future__ import annotations
from typing import Union
import math


class Vector:
    def __init__(self, x_some: float, y_some: float) -> None:
        self.x = round(x_some, 2)
        self.y = round(y_some, 2)

    def __add__(self, other: int) -> Vector:
        return Vector(
            x_some=self.x + other.x,
            y_some=self.y + other.y
        )

    def __sub__(self, other: int) -> Vector:
        return Vector(
            x_some=self.x - other.x,
            y_some=self.y - other.y,
        )

    def __mul__(self, other: int) -> Union(Vector, int):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        else:
            return Vector(
                round(self.x * other, 2), round(self.y * other, 2)
            )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> Vector:

        return cls.__sub__(Vector(*end_point), Vector(*start_point))

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        self.x = round(self.x / length, 2)
        self.y = round(self.y / length, 2)
        return self

    def angle_between(self, other: int) -> int:
        vector_modul1 = self.get_length()
        vector_modul2 = other.get_length()
        scale_dob = self.x * other.x + self.y * other.y
        cos_angle = scale_dob / (vector_modul1 * vector_modul2)
        angle = math.degrees(math.acos(cos_angle))
        return round(angle)

    def get_angle(self) -> int:
        vect = Vector(0, 1)
        angle = (self * vect) / (self.get_length() * vect.get_length())
        return round(math.degrees(math.acos(angle)))

    def rotate(self, dgreeses: int) -> Vector:
        radian = math.radians(dgreeses)
        return Vector(
            math.cos(radian) * self.x - math.sin(radian) * self.y,
            math.sin(radian) * self.x + math.cos(radian) * self.y
        )
