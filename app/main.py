from __future__ import annotations

import math


class Vector:
    def __init__(self, position_x: float, position_y: float) -> None:
        self.x = round(position_x, 2)
        self.y = round(position_y, 2)

    def __add__(self, other: Vector | float) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                self.x + other.x,
                self.y + other.y
            )

        return Vector(
            x=self.x + other,
            y=self.y + other
        )

    def __sub__(self, other: Vector | float) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                self.x - other.x,
                self.y - other.y
            )

        return Vector(
            x=self.x - other,
            y=self.y - other
        )

    def __mul__(self, other: int | float) -> Vector | float:
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            return dot_product

        return Vector(
            self.x * other,
            self.y * other
        )

    @staticmethod
    def create_vector_by_two_points(
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        position_x = end_point[0] - start_point[0]
        position_y = end_point[1] - start_point[1]
        return Vector(position_x, position_y)

    def get_length(self) -> float:
        length = math.sqrt(self.x**2 + self.y**2)
        return length

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector | float) -> int:
        if isinstance(other, Vector):
            dot = self * other
            len_self = self.get_length()
            len_other = other.get_length()
            cos_a = dot / (len_self * len_other)
            degrees = math.degrees(math.acos(cos_a))
            return round(degrees)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle_degrees: int) -> Vector:
        angle_radians = math.radians(angle_degrees)
        cos_radians = math.cos(angle_radians)
        sin_radians = math.sin(angle_radians)

        new_x = self.x * cos_radians - self.y * sin_radians
        new_y = self.x * sin_radians + self.y * cos_radians

        self.x = new_x
        self.y = new_y
        return Vector(new_x, new_y)
