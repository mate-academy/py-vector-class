from __future__ import annotations

import math
from typing import Union, Tuple


class Vector:

    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.coord_x = round(coord_x, 2)
        self.coord_y = round(coord_y, 2)

    @property
    def x(self) -> float:
        return self.coord_x

    @property
    def y(self) -> float:
        return self.coord_y

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
            self,
            other: Union[int, float, Vector]
    ) -> Union[Vector, float]:
        if isinstance(other, Vector):
            return self.dot_product(self, other)

        return Vector(round(self.x * other, 2), round(self.y * other, 2))

    def __str__(self) -> str:
        return f"Vector: x = {self.x}, y = {self.y}"

    def __repr__(self) -> str:
        return self.__str__()

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    @staticmethod
    def dot_product(vector1: Vector, vector2: Vector) -> float:
        return (vector1.x * vector2.x) + (vector1.y * vector2.y)

    def angle_between(self, other: Vector) -> float:

        dot_product = self.dot_product(self, other)
        l_1 = self.get_length()
        l_2 = other.get_length()
        return round(math.degrees(math.acos(dot_product / (l_1 * l_2))),)

    def get_normalized(self) -> Vector:
        x_normalized = round(self.x / self.get_length(), 2)
        y_normalized = round(self.y / self.get_length(), 2)
        return Vector(x_normalized, y_normalized)

    def get_angle(self) -> float:
        return round(self.angle_between(Vector(0, 1)))

    def rotate(self, degrees: Union[int, float]) -> Vector:
        cos_b = math.cos(math.radians(degrees))
        sin_b = math.sin(math.radians(degrees))
        cord_x = round((cos_b * self.x) - (sin_b * self.y), 2)
        cord_y = round((sin_b * self.x) + (cos_b * self.y), 2)
        return Vector(cord_x, cord_y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            point_a: Tuple[Union[int, float], ...],
            point_b: Tuple[Union[int, float], ...], ) -> Vector:
        x_coordinate = round(point_b[0] - point_a[0], 2)
        y_coordinate = round(point_b[1] - point_a[1], 2)
        return cls(x_coordinate, y_coordinate)
