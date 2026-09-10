from __future__ import annotations
from typing import Union
import math


class Vector:
    def __init__(self, x_coordinate: int | float,
                 y_coordinate: int | float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
            self, other: Vector | int | float
    ) -> Union[Vector, float, int]:
        if isinstance(other, int | float):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float, float],
            end_point: tuple[float, float]
    ) -> Vector:
        dx = end_point[0] - start_point[0]
        dy = end_point[1] - start_point[1]
        return cls(dx, dy)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_angle(self) -> int:
        angle = math.degrees(math.atan2(self.x, self.y))
        if angle < 0:
            angle = abs(angle)
        return round(angle)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> float:
        dot_prod = ((self.x * other.x) + (self.y * other.y))
        cos_a = dot_prod / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        new_x = (self.x * math.cos(radians)
                 - self.y * math.sin(radians))
        new_y = (self.x * math.sin(radians)
                 + self.y * math.cos(radians))
        return Vector(new_x, new_y)
