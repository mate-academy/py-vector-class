from __future__ import annotations

import math


class Vector:
    def __init__(self, x_point: float, y_point: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, (int, float)):
            return Vector(self.x * other,
                          self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return abs((self.x ** 2 + self.y ** 2) ** 0.5)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(
            self.x / length,
            self.y / length
        )

    def angle_between(self, other: Vector) -> int:
        return math.ceil(
            math.degrees(
                math.acos(
                    (self * other)
                    / (self.get_length() * other.get_length())
                )))

    def get_angle(self) -> float:
        return round(
            math.degrees(math.acos(self.y / self.get_length())),
            0
        )

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(
            math.cos(radians) * self.x - math.sin(radians) * self.y,
            math.sin(radians) * self.x + math.cos(radians) * self.y
        )

    def __repr__(self) -> str:
        return f"x={self.x}, y={self.y}"
