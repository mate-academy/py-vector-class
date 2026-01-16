from __future__ import annotations
from math import sqrt, degrees, acos, cos, sin, radians


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: Vector | int) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        x_coord = end_point[0] - start_point[0]
        y_coord = end_point[1] - start_point[1]
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length_vector = self.get_length()
        self.x = round(self.x / length_vector, 2)
        self.y = round(self.y / length_vector, 2)
        return self

    def angle_between(self, other: Vector) -> int:
        dot_product = self.x * other.x + self.y * other.y
        cos_theta = dot_product / (self.get_length() * other.get_length())
        angle_rad = acos(cos_theta)
        angle_deg = degrees(angle_rad)
        return round(angle_deg)

    def get_angle(self) -> int:
        y_vector = Vector(0, 1)
        return self.angle_between(y_vector)

    def rotate(self, degrees: int) -> Vector:
        radians_angle = radians(degrees)
        x_coord = self.x * cos(radians_angle) - self.y * sin(radians_angle)
        y_coord = self.x * sin(radians_angle) + self.y * cos(radians_angle)
        return Vector(x_coord, y_coord)
