from __future__ import annotations

import math
from math import sqrt


class Vector:
    def __init__(
            self,
            x_coordinate: int | float,
            y_coordinate: int | float
    ) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | Vector) -> Vector | float:
        if not isinstance(other, Vector):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        vector_x = end_point[0] - start_point[0]
        vector_y = end_point[1] - start_point[1]
        return cls(vector_x, vector_y)

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()
        vector_x = self.x / vector_length
        vector_y = self.y / vector_length
        return Vector(vector_x, vector_y)

    def angle_between(self, other: Vector) -> int:
        dot_product = self.x * other.x + self.y * other.y
        magnitudes_self = sqrt(self.x ** 2 + self.y ** 2)
        magnitudes_other = sqrt(other.x ** 2 + other.y ** 2)
        cos_angle = dot_product / (magnitudes_self * magnitudes_other)
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        return round(abs(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        rotation_vector_x = (self.x
                             * math.cos(radians)
                             - self.y * math.sin(radians)
                             )
        rotation_vector_y = (self.x
                             * math.sin(radians)
                             + self.y * math.cos(radians)
                             )
        return Vector(rotation_vector_x, rotation_vector_y)
