from __future__ import annotations

import math


class Vector:

    def __init__(self, x_point: float, y_point: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_point=self.x + other.x,
            y_point=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_point=self.x - other.x,
            y_point=self.y - other.y
        )

    def __mul__(self, other: Vector | int) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(
            x_point=self.x * other,
            y_point=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_pont: tuple
    ) -> Vector:
        return Vector(
            x_point=end_pont[0] - start_point[0],
            y_point=end_pont[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()

        return __class__(
            x_point=self.x / length,
            y_point=self.y / length
        )

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        if self.x == 0:
            return 0
        angle = math.atan(self.y / self.x)

        return round(math.degrees(angle) + 90)

    def rotate(self, degrees: int) -> Vector:

        angle_radians = math.radians(degrees)
        cos_theta = math.cos(angle_radians)
        sin_theta = math.sin(angle_radians)

        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta

        self.x = round(new_x, 2)
        self.y = round(new_y, 2)

        return self
