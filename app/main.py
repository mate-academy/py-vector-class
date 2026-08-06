from __future__ import annotations

import math


class Vector:
    def __init__(self, x_cor: int | float, y_cor: int | float) -> None:
        self.x = round(x_cor, 2)
        self.y = round(y_cor, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        cos_a = self.__mul__(other) / (self.get_length() * other.get_length())
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self) -> int:
        if self.x == 0:
            return 0
        angle = math.degrees(math.atan(self.y / self.x))
        return round(angle) + 90

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x_cor = math.cos(radians) * self.x - math.sin(radians) * self.y
        y_cor = math.sin(radians) * self.x + math.cos(radians) * self.y
        return Vector(x_cor, y_cor)
