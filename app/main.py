from __future__ import annotations

import math


class Vector:
    def __init__(self, x_cord: float, y_cord: float) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            round(self.x + other.x, 2),
            round(self.y + other.y, 2)
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            round(self.x - other.x, 2),
            round(self.y - other.y, 2)
        )

    def __mul__(self, other: float | int | Vector) -> float | Vector:
        if isinstance(other, (float, int)):
            return Vector(
                round(self.x * other, 2),
                round(self.y * other, 2)
            )

        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            round(end_point[0] - start_point[0], 2),
            round(end_point[1] - start_point[1], 2)
        )

    def get_length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 1:
            return self
        return Vector(
            round(self.x / length, 2),
            round(self.y / length, 2)
        )

    def angle_between(self, other: Vector) -> float:
        cos_a = self.__mul__(other) / (self.get_length() * other.get_length())
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self) -> int:
        cos_a = self.y / self.get_length()
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def rotate(self, degree: int) -> Vector:
        radians = math.radians(degree)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        x_new = self.x * cos_theta - self.y * sin_theta
        y_new = self.x * sin_theta + self.y * cos_theta
        return Vector(round(x_new, 2), round(y_new, 2))
