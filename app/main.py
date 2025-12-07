from __future__ import annotations
from typing import Union

from math import hypot, cos, sin, acos, degrees, radians


class Vector:
    def __init__(self, x_: float, y_: float) -> None:
        self.x = round(x_, 2)
        self.y = round(y_, 2)

    def __add__(self, other: Vector) -> Union[Vector, NotImplemented]:
        if isinstance(other, Vector):
            return Vector(x_=self.x + other.x, y_=self.y + other.y)
        return NotImplemented

    def __sub__(self, other: Vector) -> Union[Vector, NotImplemented]:
        if isinstance(other, Vector):
            return Vector(x_=self.x - other.x, y_=self.y - other.y)
        return NotImplemented

    def __mul__(self, other: Vector) -> Union[Vector, float, NotImplemented]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(x_=self.x * other, y_=self.y * other)
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float | int, float | int],
            end_point: tuple[float | int, float | int]
    ) -> Vector:
        return cls(
            x_=end_point[0] - start_point[0],
            y_=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ZeroDivisionError
        return Vector(x_=self.x / length, y_=self.y / length)

    def angle_between(self, vector: Vector) -> int:
        len1 = self.get_length()
        len2 = vector.get_length()

        if len1 == 0 or len2 == 0:
            raise ZeroDivisionError

        product = self * vector
        cos_theta = product / (len1 * len2)
        cos_theta = max(min(cos_theta, 1.0), -1.0)
        angle = degrees(acos(cos_theta)) % 360
        return round(angle)

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            raise ZeroDivisionError

        angle = degrees(acos(self.y / length)) % 360
        return round(angle)

    def rotate(self, degree: int) -> Vector:
        rad = radians(degree)
        return Vector(
            x_=self.x * cos(rad) - self.y * sin(rad),
            y_=self.x * sin(rad) + self.y * cos(rad),
        )
