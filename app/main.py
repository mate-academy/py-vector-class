from __future__ import annotations

import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(float(x), 2)
        self.y = round(float(y), 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )

    def __mul__(
        self, other: Vector | float
    ) -> Vector | float:
        if isinstance(other, Vector):
            return (
                self.x * other.x
                + self.y * other.y
            )
        return Vector(
            self.x * other,
            self.y * other,
        )

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float],
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0.0, 0.0)
        return Vector(
            round(self.x / length, 2),
            round(self.y / length, 2),
        )

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        lengths = (
            self.get_length() * other.get_length()
        )
        if lengths == 0:
            return 0
        cos_a = dot_product / lengths
        cos_a = max(-1.0, min(1.0, cos_a))
        angle_rad = math.acos(cos_a)
        return round(math.degrees(angle_rad))

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> Vector:
        rad = math.radians(degrees)
        cos_theta = math.cos(rad)
        sin_theta = math.sin(rad)
        new_x = (
            self.x * cos_theta
            - self.y * sin_theta
        )
        new_y = (
            self.x * sin_theta
            + self.y * cos_theta
        )
        return Vector(new_x, new_y)
