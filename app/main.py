from __future__ import annotations
from typing import Union
import math


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[int, float, Vector]) -> Vector | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> Vector | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        cos_a = (self.x * other.x + self.y * other.y) / (
            (self.get_length() * other.get_length()))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        rotate_x = self.x * math.cos(math.radians(degrees)) - (
            self.y * math.sin(math.radians(degrees))
        )
        rotate_y = self.x * math.sin(math.radians(degrees)) + (
            self.y * math.cos(math.radians(degrees))
        )
        return Vector(rotate_x, rotate_y)
