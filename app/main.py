from __future__ import annotations
from typing import Any
from math import cos, sin, radians, acos, degrees


class Vector:
    def __init__(self, coor_x: float, coor_y: float) -> None:
        self.x = round(coor_x, 2)
        self.y = round(coor_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int) -> Any:
        if isinstance(other, (int, float)):
            return Vector(other * self.x, other * self.y)

        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple,) -> Any:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        angle = round(degrees(acos(cos_a)))
        return angle

    def get_angle(self) -> float:
        cos_a = self.y / self.get_length()
        angle = round(degrees(acos(cos_a)))
        return angle

    def rotate(self, degree: int) -> Vector:
        angle = radians(degree)
        x_ = self.x * cos(angle) - self.y * sin(angle)
        y_ = self.x * sin(angle) + self.y * cos(angle)
        return Vector(x_, y_)
