from __future__ import annotations

import math


class Vector:

    def __init__(self, x_value: float, y_value: float) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | "Vector") -> float | "Vector":
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length(),
        )

    def angle_between(self, other: "Vector") -> int:
        dot = self * other
        length_mul = self.get_length() * other.get_length()
        radian_angle = math.acos(dot / length_mul)
        return round(math.degrees(radian_angle))

    def get_angle(self) -> int:
        radian_angle = math.acos(self.y / self.get_length())
        return int(math.degrees(radian_angle))

    def rotate(self, angle: int) -> "Vector":
        cos = math.cos(math.radians(angle))
        sin = math.sin(math.radians(angle))
        comp_x = self.x * cos - self.y * sin
        comp_y = self.x * sin + self.y * cos
        return Vector(comp_x, comp_y)
