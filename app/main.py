from __future__ import annotations
from typing import Union
import math


class Vector:

    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, another: Vector) -> Vector:
        return Vector(self.x + another.x, self.y + another.y)

    def __sub__(self, another: Vector) -> Vector:
        return Vector(self.x - another.x, self.y - another.y)

    def __mul__(self, another: Union[Vector, float]) -> Union[Vector, float]:
        if isinstance(another, Vector):
            return self.x * another.x + self.y * another.y
        return Vector(self.x * another, self.y * another)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple[float], end_point: tuple[float]
    ) -> Vector:
        coordinate_x = end_point[0] - start_point[0]
        coordinate_y = end_point[1] - start_point[1]
        return cls(coordinate_x, coordinate_y)

    def get_length(self) -> float:
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, another: Vector) -> int:
        length_product = self.get_length() * another.get_length()
        dot_product = self * another
        result = math.acos(dot_product / length_product)
        result_degrees = math.degrees(result)
        return round(result_degrees)

    def get_angle(self) -> int:
        positive_y = Vector(0, 1)
        dot_product = self * positive_y
        angle_radians = math.acos(dot_product / self.get_length())
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
