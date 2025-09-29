from __future__ import annotations
import math
from typing import Union


class Vector:

    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.coordinate_x = round(coordinate_x, 2)
        self.coordinate_y = round(coordinate_y, 2)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]
        return cls(new_x, new_y)

    def get_length(self) -> float:
        return math.sqrt(self.coordinate_x ** 2 + self.coordinate_y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.coordinate_x / length, self.coordinate_y / length)

    def angle_between(self, other_vector: Vector) -> int:
        dot_product = self * other_vector
        lengths_product = self.get_length() * other_vector.get_length()
        if lengths_product == 0:
            return 0
        cos_angle = max(-1.0, min(1.0, dot_product / lengths_product))
        angle = math.degrees(math.acos(cos_angle))
        return round(angle)

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> Vector:
        angle_in_radians = math.radians(degrees)
        cos_a = math.cos(angle_in_radians)
        sin_a = math.sin(angle_in_radians)
        new_x = self.coordinate_x * cos_a - self.coordinate_y * sin_a
        new_y = self.coordinate_x * sin_a + self.coordinate_y * cos_a
        return Vector(new_x, new_y)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.coordinate_x + other.coordinate_x,
            self.coordinate_y + other.coordinate_y,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.coordinate_x - other.coordinate_x,
            self.coordinate_y - other.coordinate_y,
        )

    def __mul__(self,
                other:
                Union[int, float, Vector])\
            -> Union[Vector, float]:
        return (
                self.coordinate_x * other.coordinate_x
                + self.coordinate_y * other.coordinate_y
        )
