from __future__ import annotations
import math
from typing import Union


class Vector:
    def __init__(self, x_axis: float, y_axis: float) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self,
                other: Union[Vector, int, float]) -> Union[Vector, int, float]:

        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        scalar_product = self * other
        mods_product = self.get_length() * other.get_length()
        cos = scalar_product / mods_product
        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> int:
        oy_vector = Vector(0, 1)
        return self.angle_between(oy_vector)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos = math.cos(radians)
        sin = math.sin(radians)
        x_axis = self.x * cos - self.y * sin
        y_axis = self.x * sin + self.y * cos
        return Vector(x_axis, y_axis)
