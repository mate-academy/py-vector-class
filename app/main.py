from __future__ import annotations

from numbers import Real
import math


class Vector:
    def __init__(self, x_coord: Real, y_coord: Real) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x_coord=self.x + other.x, y_coord=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x_coord=self.x - other.x, y_coord=self.y - other.y)

    def __mul__(self, other: Vector | Real) -> Vector | Real:
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            return dot_product

        if isinstance(other, Real):
            return Vector(x_coord=self.x * other, y_coord=self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(x_coord=end_point[0] - start_point[0],
                   y_coord=end_point[1] - end_point[1])

    def get_length(self) -> Real:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(x_coord=self.x / self.get_length(),
                      y_coord=self.y / self.get_length())

    def angle_between(self, other: Vector) -> Real:
        dot_product = self * other
        self_length = self.get_length()
        other_length = other.get_length()

        cos_theta = dot_product / (self_length * other_length)

        return round(math.degrees(math.acos(cos_theta)))

    def get_angle(self) -> Real:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: Real) -> Vector:
        cos = math.cos(math.radians(degrees))
        sin = math.sin(math.radians(degrees))
        rotated_vector_x = (cos * self.x) - (sin * self.y)
        rotated_vector_y = (sin * self.x) + (cos * self.y)
        return Vector(rotated_vector_x, rotated_vector_y)
