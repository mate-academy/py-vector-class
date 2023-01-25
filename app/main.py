from __future__ import annotations
from typing import Union
from math import sqrt, acos, degrees, sin, cos, atan2, radians, ceil


class Vector:

    def __init__(self, x_axis: float, y_axis: float) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[Vector, float]) -> Union[Vector, float]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        x_axis = end_point[0] - start_point[0]
        y_axis = end_point[1] - start_point[1]
        return Vector(x_axis, y_axis)

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        if isinstance(other, Vector):
            return ceil(
                degrees(
                    acos(
                        (self * other)
                        / (self.get_length() * other.get_length())
                    )
                )
            )

    def get_angle(self) -> int:
        return int(abs(degrees(atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        radian = radians(degrees)
        x_axis = self.x * cos(radian) - self.y * sin(radian)
        y_axis = self.x * sin(radian) + self.y * cos(radian)
        return Vector(x_axis, y_axis)
