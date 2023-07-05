from __future__ import annotations
from typing import Optional
import math


class Vector:
    def __init__(self, x_: float, y_: float) -> None:
        self.x = round(x_, 2)
        self.y = round(y_, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
            self,
            other: Optional[int, float, Vector]
    ) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return pow(pow(self.x, 2) + pow(self.y, 2), 1 / 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        mul_vectors = self * other
        mul_vectors_len = self.get_length() * other.get_length()
        radian_angle = math.acos(mul_vectors / mul_vectors_len)
        angle = round(math.degrees(radian_angle))
        return angle

    def get_angle(self) -> int:
        vector_y = Vector(0, 1)
        return self.angle_between(vector_y)

    def rotate(self, degrees: int) -> Vector:
        degrees = math.radians(degrees)
        x_ = math.cos(degrees) * self.x - math.sin(degrees) * self.y
        y_ = math.sin(degrees) * self.x + math.cos(degrees) * self.y
        return Vector(x_, y_)
