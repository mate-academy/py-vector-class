from __future__ import annotations
from typing import Union
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: Union[float, Vector]) -> Union[Vector, float]:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector((self.x * other), (self.y * other))

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / Vector.get_length(self),
                      self.y / Vector.get_length(self))

    def angle_between(self, vector2: tuple) -> int:
        if isinstance(vector2, Vector):
            cos_a = Vector.__mul__(self, vector2)\
                / (Vector.get_length(self) * Vector.get_length(vector2))
            return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = self.y / Vector.get_length(self)
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> Vector:
        x = round(math.cos(math.radians(degrees))
                  * self.x - math.sin(math.radians(degrees)) * self.y, 2)
        y = round(math.sin(math.radians(degrees))
                  * self.x + math.cos(math.radians(degrees)) * self.y, 2)
        return Vector(x, y)
