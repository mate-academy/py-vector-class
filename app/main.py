from __future__ import annotations
from math import sqrt
import math


class Vector:
    def __init__(self, x_value: (int, float), y_value: (int, float)) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_value=self.x + other.x,
            y_value=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_value=self.x - other.x,
            y_value=self.y - other.y
        )

    def __mul__(self, other: (int, float, Vector)) -> (Vector, int, float):
        if isinstance(other, (int, float)):
            return Vector(
                x_value=self.x * other,
                y_value=self.y * other
            )
        else:
            print(self.x)
            print(other.x)
            dot_product = (self.x * other.x) + (self.y * other.y)
            return dot_product

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return cls(
            x_value=end[0] - start[0],
            y_value=end[1] - start[1]
        )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        x_value = round((self.x / self.get_length()), 2)
        y_value = round((self.y / self.get_length()), 2)
        return Vector(x_value, y_value)

    def angle_between(self, other: Vector) -> int:
        cos = ((self.x * other.x + self.y * other.y)
               / (self.get_length() * other.get_length()))
        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> int:
        angle = (self.y / self.get_length())
        return int(math.degrees(math.acos(angle)))

    def rotate(self, angle: int) -> Vector:
        return Vector(
            x_value=round((self.x * (math.cos(math.radians(angle)))
                           - self.y * (math.sin(math.radians(angle)))), 2),
            y_value=round((self.y * (math.cos(math.radians(angle)))
                           + self.x * (math.sin(math.radians(angle)))), 2)
        )
