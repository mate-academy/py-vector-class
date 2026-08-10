from __future__ import annotations
from typing import Self
import math


class Vector:
    def __init__(self, coor_x: float, coor_y: float) -> None:
        self.x = round(coor_x, 2)
        self.y = round(coor_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if not isinstance(other, Vector):
            return Vector(self.x * other, self.y * other)
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple,
    ) -> Self:
        return cls(
            end_point[0]
            - start_point[0],
            end_point[1]
            - start_point[1]
        )

    def get_length(self) -> float:
        result = math.sqrt(self.x ** 2 + self.y ** 2)
        return result

    def get_normalized(self) -> Vector:
        v_norm = math.sqrt(self.x ** 2 + self.y ** 2)
        x_norm = self.x / v_norm
        y_norm = self.y / v_norm
        return Vector(x_norm, y_norm)

    def angle_between(self, other: Vector) -> int:
        dot_sum = (self.x * other.x) + (self.y * other.y)
        long_first_vector = math.sqrt(self.x ** 2 + self.y ** 2)
        long_second_vector = math.sqrt(other.x ** 2 + other.y ** 2)
        cos_angle = dot_sum / (long_first_vector * long_second_vector)
        angle_rad = math.acos(cos_angle)
        degree_angle = math.degrees(angle_rad)
        return round(degree_angle)

    def get_angle(self) -> int:
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        cos_a = self.y / length
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
