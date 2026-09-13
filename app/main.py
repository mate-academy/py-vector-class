from __future__ import annotations
from math import acos, cos, degrees, radians, sin


class Vector:

    def __init__(
        self,
        x_cord: int | float,
        y_cord: int | float
    ) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x_cord=self.x + other.x, y_cord=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x_cord=self.x - other.x, y_cord=self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> int | float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(x_cord=self.x * other, y_cord=self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return cls(x_cord=end[0] - start[0], y_cord=end[1] - start[1])

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        le = self.get_length()
        return Vector(x_cord=self.x / le, y_cord=self.y / le)

    def angle_between(self, other: Vector) -> int:
        if self.get_length() == 0 or other.get_length() == 0:
            raise ZeroDivisionError
        return round(
            degrees(
                acos(
                    self * other / (self.get_length() * other.get_length())))
        )

    def get_angle(self) -> int:
        return self.angle_between(Vector(x_cord=0, y_cord=1))

    def rotate(self, degrees: int | float) -> Vector:
        angle = radians(degrees)
        new_x = self.x * cos(angle) - self.y * sin(angle)
        new_y = self.x * sin(angle) + self.y * cos(angle)
        return Vector(x_cord=new_x, y_cord=new_y)
