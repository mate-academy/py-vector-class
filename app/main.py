from __future__ import annotations

import math


class Vector:
    def __init__(self, x: float | int, y: float | int) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        length = self.get_length()

        if length == 0:
            raise ZeroDivisionError

        return Vector(
            self.x / length,
            self.y / length
        )

    def angle_between(self, other: Vector) -> int:
        denominator = self.get_length() * other.get_length()

        if denominator == 0:
            raise ValueError()

        cos_a = (self * other) / denominator
        cos_a = max(-1.0, min(1.0, cos_a))

        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, angle: float) -> Vector:
        radians = math.radians(angle)
        cos_val = math.cos(radians)
        sin_val = math.sin(radians)

        new_x = self.x * cos_val - self.y * sin_val
        new_y = self.x * sin_val + self.y * cos_val

        return Vector(new_x, new_y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float, float],
            end_point: tuple[float, float]
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )
