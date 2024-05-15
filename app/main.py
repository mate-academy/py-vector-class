from __future__ import annotations

import math


class Vector:
    def __init__(self, x_side: int | float, y_side: int | float) -> None:
        self.x = round(x_side, 2)
        self.y = round(y_side, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        return round(
            math.degrees(
                math.acos(
                    (self * other) / (self.get_length() * other.get_length())
                )
            )
        )

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        angle = math.radians(degrees)
        x_side = self.x * math.cos(angle) - self.y * math.sin(angle)
        y_side = self.x * math.sin(angle) + self.y * math.cos(angle)
        return Vector(x_side, y_side)
