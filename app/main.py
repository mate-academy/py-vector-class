from __future__ import annotations

import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        x_coordinate = round(self.x + other.x, 2)
        y_coordinate = round(self.y + other.y, 2)

        return Vector(x_coordinate, y_coordinate)

    def __sub__(self, other: Vector) -> Vector:
        x_coordinate = round(self.x - other.x, 2)
        y_coordinate = round(self.y - other.y, 2)

        return Vector(x_coordinate, y_coordinate)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            x_coordinate = self.x * other.x
            y_coordinate = self.y * other.y
            result = x_coordinate + y_coordinate
            return result
        else:
            x_coordinate = round(self.x * other, 2)
            y_coordinate = round(self.y * other, 2)
            return Vector(x_coordinate, y_coordinate)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:

        return cls(*end_point) - cls(*start_point)

    def get_length(self) -> float:
        length = (self.x ** 2 + self.y ** 2) ** 0.5

        return length

    def get_normalized(self) -> Vector:
        length = self.get_length()

        normalize_x = self.x / length
        normalize_y = self.y / length

        return Vector(round(normalize_x, 2), round(normalize_y, 2))

    def angle_between(self, vector: Vector) -> int:
        length_v1 = self.get_length()
        length_v2 = vector.get_length()

        dot_product = self.dot_product(self, vector)

        cosine_theta = dot_product / (length_v1 * length_v2)
        angle_radians = math.acos(cosine_theta)
        angle_degrees = math.degrees(angle_radians)

        return round(angle_degrees)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: int) -> Vector:
        angle_radians = math.radians(angle)

        sin = math.sin(angle_radians)
        cos = math.cos(angle_radians)

        x_rotated = cos * self.x - sin * self.y
        y_rotated = sin * self.x + cos * self.y

        return Vector(round(x_rotated, 2), round(y_rotated, 2))

    @staticmethod
    def dot_product(vector1: Vector, vector2: Vector) -> float:
        dot_product = (vector1.x * vector2.x + vector1.y * vector2.y)
        return dot_product
