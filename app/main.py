from __future__ import annotations
from typing import Union
import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[Vector, float, int]) -> \
            Union[Vector, float, int]:
        if not isinstance(other, Vector):
            return Vector(self.x * other, self.y * other)
        dot_product = self.x * other.x + self.y * other.y
        return dot_product

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        normalized = math.sqrt(self.x * self.x + self.y * self.y)
        x_coordinate = self.x / normalized
        y_coordinate = self.y / normalized
        return Vector(x_coordinate, y_coordinate)

    def angle_between(self, other: Vector) -> int:
        dot_product = self.x * other.x + self.y * other.y
        mod_a = math.sqrt(self.x ** 2 + self.y ** 2)
        mod_b = math.sqrt(other.x ** 2 + other.y ** 2)
        cos_a = dot_product / (mod_a * mod_b)
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self) -> int:
        dot_product = self.x * 0 + self.y * 1
        mod_a = math.sqrt(self.x ** 2 + self.y ** 2)
        mod_b = math.sqrt(0 ** 2 + 1 ** 2)
        cos_a = dot_product / (mod_a * mod_b)
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def rotate(self, degrees: int) -> Vector:
        radian = math.radians(degrees)
        x_coordinate = self.x * math.cos(radian) - self.y * math.sin(radian)
        y_coordinate = self.x * math.sin(radian) + self.y * math.cos(radian)
        return Vector(x_coordinate, y_coordinate)
