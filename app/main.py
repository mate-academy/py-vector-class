from __future__ import annotations

import math


class Vector:
    def __init__(self, x_cord: int | float, y_cord: float | int) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> Vector:
        first_x, first_y, second_x, second_y = *start_point, *end_point
        return cls(second_x - first_x, second_y - first_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        self_length = self.get_length()
        other_length = Vector.get_length(other)

        if self_length and other_length:
            cosine = self.__mul__(other) / (self_length * other_length)
            return int(round(math.degrees(math.acos(cosine))))

    def get_angle(self) -> int:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        cosine = math.cos(math.radians(degrees))
        sinus = math.sin(math.radians(degrees))
        return Vector(
            self.x * cosine - self.y * sinus,
            self.x * sinus + self.y * cosine)
