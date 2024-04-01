from __future__ import annotations
import math
from math import sqrt, ceil, acos, radians, cos, sin


class Vector:
    def __init__(self, var_x: int | float, var_y: int | float) -> None:
        self.x = round(var_x, 2)
        self.y = round(var_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point:
                                    tuple, end_point: tuple) -> Vector:
        vector_start = cls(start_point[0], start_point[1])
        vector_end = cls(end_point[0], end_point[1])
        return cls(vector_end.x - vector_start.x,
                   vector_end.y - vector_start.y)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(),
                      self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        upper = (self.x * other.x) + (self.y * other.y)
        down = (sqrt(self.x ** 2 + self.y ** 2)) * \
               (sqrt(other.x ** 2 + other.y ** 2))
        return ceil(math.degrees(acos(upper / down)))

    def get_angle(self) -> int:
        other = Vector(0, 1)
        upper = (self.x * other.x) + (self.y * other.y)
        down = (sqrt(self.x ** 2 + self.y ** 2)) * \
               (sqrt(other.x ** 2 + other.y ** 2))
        return round(math.degrees(acos(upper / down)))

    def rotate(self, degrees: int) -> Vector:
        degrees = radians(degrees)
        vector_x_2 = (self.x * cos(degrees) - self.y * sin(degrees))
        vector_y_2 = (self.y * cos(degrees) + self.x * sin(degrees))
        return Vector(vector_x_2, vector_y_2)
