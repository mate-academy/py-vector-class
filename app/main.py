from __future__ import annotations

import math


class Vector:
    def __init__(self, coor_x: float, coor_y: float) -> None:
        self.x = round(coor_x, 2)
        self.y = round(coor_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

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
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector | None:
        length = self.get_length()
        if length != 0:
            return Vector(self.x / length, self.y / length)
        return None

    def angle_between(self, other: Vector) -> float:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float | None:
        if self.get_length() != 0:
            cos_a = self * Vector(0, 1) / self.get_length()
            return round(math.degrees(math.acos(cos_a)))
        return None

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(
            self.x * math.cos(radians) - self.y * math.sin(radians),
            self.y * math.cos(radians) + self.x * math.sin(radians)
        )
