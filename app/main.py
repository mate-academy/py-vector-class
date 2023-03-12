from __future__ import annotations
import math
from typing import Union, Any


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x=x, y=y)

    def __sub__(self, other: Vector) -> Vector:
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x=x, y=y)

    def __mul__(self, other: Union[int, float, Vector]) -> Any:
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            return dot_product
        x = self.x * other
        y = self.y * other
        return Vector(x=x, y=y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple)\
            -> Vector:
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(x, y)

    def get_length(self) -> float:
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self) -> Vector:
        length = self.get_length()
        x = round(self.x / length, 2)
        y = round(self.y / length, 2)
        return Vector(x=x, y=y)

    def angle_between(self, other: Vector) -> int:
        cos_a = self.__mul__(other) / self.get_length() / other.get_length()
        return int(round(math.degrees(math.acos(cos_a)), 0))

    def get_angle(self) -> int:
        y = abs(self.y)
        other = Vector(x=0, y=y)
        return self.angle_between(other)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x = round(self.x * math.cos(radians) - self.y * math.sin(radians), 2)
        y = round(self.x * math.sin(radians) + self.y * math.cos(radians), 2)
        return Vector(x=x, y=y)
