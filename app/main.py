from __future__ import annotations

import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x_coord=self.x + other.x, y_coord=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x_coord=self.x - other.x, y_coord=self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, (float, int)):
            return Vector(x_coord=self.x * other, y_coord=self.y * other)
        else:
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(x_coord=end_point[0] - start_point[0],
                   y_coord=end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(x_coord=self.x / length, y_coord=self.y / length)

    def angle_between(self, other: Vector) -> int:
        self_length = self.get_length()
        other_length = other.get_length()
        dot_product = self * other
        return round(
            math.degrees(
                math.acos(
                    dot_product / (self_length * other_length))))

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        self_length = self.get_length()
        y_length = y_axis.get_length()
        dot_product = self * y_axis
        return round(
            math.degrees(
                math.acos(
                    dot_product / (self_length * y_length))))

    def rotate(self, degrees: int) -> Vector:
        cos = math.cos(math.radians(degrees))
        sin = math.sin(math.radians(degrees))
        return Vector(x_coord=cos * self.x - sin * self.y,
                      y_coord=sin * self.x + cos * self.y)
