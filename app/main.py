from __future__ import annotations
import math


class Vector:

    def __init__(self, x_: float, y_: float) -> None:
        self.x = round(x_, 2)
        self.y = round(y_, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | int:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return cls(end[0] - start[0], end[1] - start[1])

    def get_length(self) -> float:
        return pow(self.x ** 2 + self.y ** 2, 0.5)

    def get_normalized(self) -> Vector:
        len_ = self.get_length()
        return Vector(self.x / len_, self.y / len_)

    def angle_between(self, other: Vector) -> int:
        cos = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 10))

    def rotate(self, degrees: int) -> Vector:
        cos = math.cos(math.radians(degrees))
        sin = math.sin(math.radians(degrees))
        new_x = self.x * cos - self.y * sin
        new_y = self.x * sin + self.y * cos
        return Vector(new_x, new_y)
