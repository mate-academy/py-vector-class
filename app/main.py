from __future__ import annotations
from typing import Union
import math


class Vector:
    def __init__(self, x_value: float, y_value: float) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[Vector, int, float]) \
            -> Union[Vector, int, float]:
        if isinstance(other, Vector):
            # a · b = ax × bx + ay × by
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()
        return Vector(round(self.x / vector_length, 2),
                      round(self.y / vector_length, 2))

    def angle_between(self, other: Vector) -> int:
        # cos = (u * v) / (|u| * |v|)
        cos = (self.x * other.x
               + self.y * other.y) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(math.cos(radians) * self.x - math.sin(radians) * self.y,
                      math.sin(radians) * self.x + math.cos(radians) * self.y)
