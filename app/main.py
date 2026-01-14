from __future__ import annotations

import math


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple,
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return abs((self.x ** 2 + self.y ** 2) ** 0.5)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        coord_x = round(self.x / length, 2)
        coord_y = round(self.y / length, 2)

        return Vector(coord_x, coord_y)

    def angle_between(self, other: Vector) -> int:
        self_len = self.get_length()
        other_len = other.get_length()
        scalar_prod = self.x * other.x + self.y * other.y
        angle = math.degrees(math.acos(scalar_prod / (self_len * other_len)))

        return round(angle)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        cos_of_angle = math.cos(math.radians(degrees))
        sin_of_angle = math.sin(math.radians(degrees))
        coord_x = round(self.x * cos_of_angle - self.y * sin_of_angle, 2)
        coord_y = round(self.x * sin_of_angle + self.y * cos_of_angle, 2)

        return Vector(coord_x, coord_y)
