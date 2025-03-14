from __future__ import annotations

import math


class Vector:
    def __init__(self, x_val: int | float, y_val: int | float) -> None:
        self.x = round(x_val, 2)
        self.y = round(y_val, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float) -> Vector | float:
        return (
            self.x * other.x + self.y * other.y
            if isinstance(other, Vector)
            else Vector(self.x * other, self.y * other)
        )

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        dot = self * other
        norm_self = self.get_length()
        norm_other = other.get_length()

        cos_a = dot / (norm_self * norm_other)
        cos_a = max(-1, min(1, cos_a))

        angle_deg = math.degrees(math.acos(cos_a))
        return round(angle_deg)

    def get_angle(self) -> int:
        norm = self.get_length()

        cos_angle = self.y / norm
        cos_angle = max(-1, min(1, cos_angle))
        angle_deg = math.degrees(math.acos(cos_angle))
        return round(angle_deg)

    def rotate(self, degrees: int) -> Vector:
        rad = math.radians(degrees)
        cos_theta = math.cos(rad)
        sin_theta = math.sin(rad)
        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta
        return Vector(new_x, new_y)
