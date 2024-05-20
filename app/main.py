from __future__ import annotations
from math import sqrt
from math import acos, degrees, cos, sin, radians


class Vector:
    def __init__(self, cord_x: float, cord_y: float) -> None:
        self.x = round(cord_x, 2)
        self.y = round(cord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return other.x * self.x + other.y * self.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return Vector(end[0] - start[0], end[1] - start[1])

    def get_length(self) -> float:
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self) -> Vector:
        magnitude = sqrt(pow(self.x, 2) + pow(self.y, 2))
        return Vector(self.x / magnitude, self.y / magnitude)

    def angle_between(self, vector: Vector) -> int:
        dot_product = vector.x * self.x + vector.y * self.y
        norm_product = vector.get_length() * self.get_length()
        return round(degrees(acos(dot_product / norm_product)))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angel: int) -> Vector:
        rad = radians(angel)
        cos_theta = cos(rad)
        sin_theta = sin(rad)

        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta

        return Vector(new_x, new_y)
