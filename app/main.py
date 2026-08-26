from __future__ import annotations

import math


class Vector:
    __Y_AXIS: Vector = None

    @staticmethod
    def get_y_axis() -> Vector:
        if not Vector.__Y_AXIS:
            Vector.__Y_AXIS = Vector(0, 1)

        return Vector.__Y_AXIS

    def __init__(self, x_value: float, y_value: float) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return self + other * -1

    def __mul__(self, other: float | int | Vector) -> Vector | float:
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)

        return self.x * other.x + self.y * other.y

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

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()

        return Vector(
            self.x / length,
            self.y / length
        )

    def angle_between(self, other: Vector) -> float:
        cos_a = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        return Vector.get_y_axis().angle_between(self)

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        sin = math.sin(radians)
        cos = math.cos(radians)

        return Vector(
            self.x * cos - self.y * sin,
            self.x * sin + self.y * cos
        )
