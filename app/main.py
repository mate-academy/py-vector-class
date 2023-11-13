from __future__ import annotations
from math import acos, cos, degrees, radians, sin, sqrt


class Vector:

    def __init__(self, coordinate_x: int, coordinate_y: int) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> int | float | Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_points: tuple,
            end_points: tuple
    ) -> Vector:
        return Vector(
            end_points[0] - start_points[0],
            end_points[1] - start_points[1]
        )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length != 0:
            return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            magnitudes_product = self.get_length() * other.get_length()
            angle = dot_product / magnitudes_product
            return round(degrees(acos(angle)))

    def get_angle(self) -> int:
        if self.y > 0:
            other = Vector(0, self.y)
        else:
            other = Vector(0, -self.y)
        return self.angle_between(other)

    def rotate(self, degrees: int) -> Vector:
        radians_value = radians(degrees)
        rotate_x = self.x * cos(radians_value) - self.y * sin(radians_value)
        rotate_y = self.x * sin(radians_value) + self.y * cos(radians_value)
        return Vector(rotate_x, rotate_y)
