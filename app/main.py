from __future__ import annotations
from math import acos, cos, degrees, radians, sqrt, sin


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

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

    def __mul__(self, other: int | float | Vector) -> Vector:
        if isinstance(other, (int, float)):
            return Vector(
                (self.x * other),
                (self.y * other)
            )
        return (self.x * other.x + self.y * other.y)

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> Vector:
        x1, y1 = start_point
        x2, y2 = end_point

        return cls(x2 - x1, y2 - y1)

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        length_self = self.get_length()
        length_other = other.get_length()

        cos_theta = max(
            -1.0,
            min(
                1.0,
                dot_product / (length_self * length_other)
            )
        )
        angle = degrees(acos(cos_theta))

        return round(angle)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        degrees_rad = radians(degrees)
        rotated_x = cos(degrees_rad) * self.x - sin(degrees_rad) * self.y
        rotates_y = sin(degrees_rad) * self.x + cos(degrees_rad) * self.y

        return Vector(rotated_x, rotates_y)
