from __future__ import annotations

import math
from math import acos, cos, radians, sin, sqrt, degrees


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Addition with unsupported type.")

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        raise TypeError("Subtraction with unsupported type.")

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point : tuple,
                                    end_point : tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = sqrt(self.x ** 2 + self.y ** 2)
        normalized_x = self.x / length
        normalized_y = self.y / length
        return Vector(normalized_x, normalized_y)

    def angle_between(self, other: Vector) -> float:
        dot_product = self.x * other.x + self.y * other.y
        magnitude_self = math.sqrt(self.x**2 + self.y**2)
        magnitude_other = math.sqrt(other.x**2 + other.y**2)
        angle = round(degrees(acos(dot_product
                                   / (magnitude_self * magnitude_other))))
        return angle

    def get_angle(self) -> float:
        positive_y_axis = (0, 1)
        dot_product = self.x * positive_y_axis[0] + self.y * positive_y_axis[1]
        magnitude = sqrt(self.x**2 + self.y**2)
        angle = round(degrees(acos(dot_product / magnitude)))
        return angle

    def rotate(self, degrees: float) -> Vector:
        new_x = self.x * cos(radians(degrees)) - self.y * sin(radians(degrees))
        new_y = self.x * sin(radians(degrees)) + self.y * cos(radians(degrees))
        return Vector(new_x, new_y)
