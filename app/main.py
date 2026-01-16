from __future__ import annotations

import math


class Vector:

    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector) -> float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            return dot_product

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple)\
            -> Vector:
        return cls(list(end_point)[0] - list(start_point)[0],
                   list(end_point)[1] - list(start_point)[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        inv_length = 1 / self.get_length()
        return Vector(self.x * inv_length, self.y * inv_length)

    def angle_between(self, other: Vector) -> float:
        mul_vectors = self * other
        cos_a = mul_vectors / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degree: int) -> Vector:
        rezalt_x = self.x * math.cos(math.radians(degree)) - self.y * math.sin(
            math.radians(degree))
        rezalt_y = self.x * math.sin(math.radians(degree)) + self.y * math.cos(
            math.radians(degree))
        return Vector(rezalt_x, rezalt_y)
