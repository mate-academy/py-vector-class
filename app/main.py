from __future__ import annotations
import math
from typing import Union


class Vector:
    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[Vector, float, int]) -> Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: [Vector, float]) -> float:
        cos_a = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(
            math.cos(radians) * self.x - math.sin(radians) * self.y,
            math.sin(radians) * self.x + math.cos(radians) * self.y,
        )
