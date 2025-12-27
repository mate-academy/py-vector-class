from __future__ import annotations
import math


class Vector:
    def __init__(self, vector_x: int | float, vector_y: int | float) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(vector_x=self.x + other.x, vector_y=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(vector_x=self.x - other.x, vector_y=self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(vector_x=self.x * other, vector_y=self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple,
            end_point: tuple) -> Vector:
        x1, y1 = start_point
        x2, y2 = end_point
        return cls(vector_x=x2 - x1, vector_y=y2 - y1)

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(vector_x=self.x / self.get_length(),
                      vector_y=self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        answer = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(answer)))

    def get_angle(self) -> int:
        y_axis = Vector(vector_x=0, vector_y=1)
        answer = self * y_axis / self.get_length()
        return round(math.degrees(math.acos(answer)))

    def rotate(self, degree: int) -> Vector:
        cos_degree = math.cos(math.radians(degree))
        sin_degree = math.sin(math.radians(degree))
        x_rotated = self.x * cos_degree - self.y * sin_degree
        y_rotated = self.x * sin_degree + self.y * cos_degree
        return Vector(vector_x=x_rotated, vector_y=y_rotated)
