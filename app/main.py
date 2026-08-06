from __future__ import annotations
from typing import Union
import math


class Vector:
    def __init__(self, x_axit: float, y_axit: float) -> None:
        self.x = round(x_axit, 2)
        self.y = round(y_axit, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_axit=self.x + other.x,
            y_axit=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_axit=self.x - other.x,
            y_axit=self.y - other.y
        )

    def __mul__(self, other: Union) -> Union:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_pont: tuple) -> Vector:
        return Vector(end_pont[0] - start_point[0],
                      end_pont[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        cos_a = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, other: int) -> Vector:
        return Vector((math.cos(math.radians(other)) * self.x)
                      - (math.sin(math.radians(other)) * self.y),
                      (math.sin(math.radians(other)) * self.x)
                      + (math.cos(math.radians(other)) * self.y))
