from __future__ import annotations

import math


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

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

    def __mul__(self, other: Vector | int | float) -> Vector | float | int:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> int:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        inv_length = 1 / self.get_length()
        return Vector(self.x * inv_length, self.y * inv_length)

    def angle_between(self, other: Vector) -> int:
        cos_ = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_)))

    def rotate(self, degrees: int | float) -> Vector:
        radians = math.radians(degrees)
        rotated_x = (self.x * math.cos(radians)
                     - self.y * math.sin(radians))
        rotated_y = (self.x * math.sin(radians)
                     + self.y * math.cos(radians))
        return Vector(rotated_x, rotated_y)

    def get_angle(self) -> int:
        cos_y = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_y)))
