from __future__ import annotations

import math


class Vector:

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(round(self.x * other, 2), round(self.y * other, 2))

    def get_length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def get_normalized(self) -> Vector:
        if self.get_length() == 0:
            return Vector(0, 0)
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other: Vector) -> float:
        dot_p = self * other
        mag_p_a = self.get_length()
        mag_p_b = other.get_length()
        cos_theta = dot_p / (mag_p_a * mag_p_b)
        cos_theta = max(-1, min(1, cos_theta))
        theta = math.acos(cos_theta)
        return round(math.degrees(theta))

    def get_angle(self) -> float:
        cos_theta = self.y / self.get_length()
        cos_theta = max(-1, min(1, cos_theta))
        theta = math.acos(cos_theta)
        return round(math.degrees(theta))

    def rotate(self, degrees: int) -> Vector:
        angle_rad = math.radians(degrees)
        new_x = self.x * math.cos(angle_rad) - self.y * math.sin(angle_rad)
        new_y = self.x * math.sin(angle_rad) + self.y * math.cos(angle_rad)
        return Vector(round(new_x, 2), round(new_y, 2))
