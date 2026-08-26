from __future__ import annotations

import math


class Vector:
    def __init__(self, x_axis: int | float, y_axis: int | float) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(round(self.x + other.x, 2), round(self.y + other.y, 2))

    def __sub__(self, other: Vector) -> Vector:
        return Vector(round(self.x - other.x, 2), round(self.y - other.y, 2))

    def __mul__(self, other: Vector | int | float) -> Vector | float | int:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector((self.x * other), (self.y * other))

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> int:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def dot_product(self, other: Vector) -> int:
        return self.x * other.x + self.y * other.y

    def lengths_product(self, other: Vector) -> int:
        return self.get_length() * other.get_length()

    def angle_between(self, other: Vector) -> int:
        return round(
            math.degrees(
                math.acos(self.dot_product(other)
                          / self.lengths_product(other))
            )
        )

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cs = math.cos(radians)
        sn = math.sin(radians)

        x_axis = self.x * cs - self.y * sn
        y_axis = self.x * sn + self.y * cs

        return Vector(x_axis, y_axis)
