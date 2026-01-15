# flake8: noqa: VNE001
from __future__ import annotations
from math import degrees, acos, cos, radians, sin, sqrt


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x=self.x - other.x, y=self.y - other.y)

    def __mul__(self, other: float | int | Vector) -> float | Vector:
        if isinstance(other, (float, int)):
            return Vector(x=self.x * other, y=self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return Vector(
            x=end_point[0] - start_point[0], y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(x=round(self.x / length, 2), y=round(self.y / length, 2))

    def angle_between(self, other: Vector) -> int:
        return round(
            degrees(
                acos(
                    (self.x * other.x + self.y * other.y)
                    / (self.get_length() * other.get_length())
                )
            )
        )

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        dot_product = self * y_axis
        self_magnitude = sqrt(self.x**2 + self.y**2)
        y_axis_magnitude = sqrt(y_axis.x**2 + y_axis.y**2)
        cos_a = dot_product / (self_magnitude * y_axis_magnitude)
        angle_rad = acos(cos_a)
        angle_deg = degrees(angle_rad)
        return round(angle_deg)

    def rotate(self, degrees: int) -> Vector:
        rad = radians(degrees)
        return Vector(
            x=self.x * cos(rad) - self.y * sin(rad),
            y=self.x * sin(rad) + self.y * cos(rad),
        )
