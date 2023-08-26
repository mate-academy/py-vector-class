from __future__ import annotations
from typing import Union
import math


class Vector:

    def __init__(
            self,
            x_coordinate: Union[int, float],
            y_coordinate: Union[int, float]
    ) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(
            self,
            other: Union[Vector, int, float]
    ) -> Union[Vector, int, float]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError("Unsupported operand type for *")

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        vector_x = end_point[0] - start_point[0]
        vector_y = end_point[1] - start_point[1]
        return cls(vector_x, vector_y)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = self.x * other.x + self.y * other.y
        self_length = self.get_length()
        other_length = other.get_length()
        cos_angle = dot_product / (self_length * other_length)
        angle_radians = math.acos(cos_angle)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def get_angle(self) -> int:
        angle_rad = math.atan2(self.x, self.y)
        angle_deg = math.degrees(angle_rad)
        return abs(round(angle_deg))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
