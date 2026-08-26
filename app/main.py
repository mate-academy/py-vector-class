from __future__ import annotations
from math import sqrt, degrees, acos, radians, cos, sin


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            dot_product = ((self.x * other.x) + (self.y * other.y))
            return dot_product
        return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        x_vector = end_point[0] - start_point[0]
        y_vector = end_point[1] - start_point[1]
        return cls(x_vector, y_vector)

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        self_length = self.get_length()
        other_length = other.get_length()
        cos_a = dot_product / (self_length * other_length)
        return round(degrees(acos(cos_a)))

    def get_angle(self) -> int:
        length = self.get_length()
        return round(degrees(acos(self.y / length)))

    def rotate(self, degrees: int) -> Vector:
        angle = radians(degrees)
        new_x = round(self.x * cos(angle) - self.y * sin(angle), 2)
        new_y = round(self.x * sin(angle) + self.y * cos(angle), 2)
        return Vector(new_x, new_y)
