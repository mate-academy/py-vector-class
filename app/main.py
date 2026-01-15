from __future__ import annotations
import math
from typing import Union


class Vector:
    def __init__(
            self, x_coord: float | int, y_coord: float | int
    ) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other : Vector) -> Vector:
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other : Vector) -> Vector:
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(
            self, other: Union[Vector, float, int]
    ) -> Vector | float | int:
        if isinstance(other, Vector):
            return ((self.x * other.x) + (self.y * other.y))
        if isinstance(other, Union[int, float]):
            new_x = self.x * other
            new_y = self.y * other
            return Vector(new_x, new_y)

    @classmethod
    def create_vector_by_two_points(
        cls, first_point: tuple, second_point: tuple
    ) -> Vector:
        x_coord = second_point[0] - first_point[0]
        y_coord = second_point[1] - first_point[1]
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()
        if vector_length != 0:
            normalized_x = self.x / vector_length
            normalized_y = self.y / vector_length
            return Vector(normalized_x, normalized_y)

    def angle_between(self, other: Vector) -> int | float:
        dot_product = self.__mul__(other)
        vectors_magnitude = self.get_length() * other.get_length()
        cos_theta = dot_product / vectors_magnitude
        theta = math.acos(cos_theta)
        return round(math.degrees(theta))

    def get_angle(self) -> int:
        positive_y_vector = Vector(0, 1)
        return self.angle_between(positive_y_vector)

    def rotate(self, degree: int) -> Vector:
        radians = math.radians(degree)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
