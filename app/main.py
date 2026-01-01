# flake8: noqa: E741

from __future__ import annotations

import math
from typing import Union

Number = Union[int, float]


def _round2(value: Number) -> float:
    return round(float(value), 2)


class Vector:
    def __init__(self, x: Number, y: Number) -> None:
        self.x = _round2(x)
        self.y = _round2(y)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union["Vector", Number]) -> Union["Vector", float]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        multiplier = float(other)
        return Vector(self.x * multiplier, self.y * multiplier)

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[Number, Number],
        end_point: tuple[Number, Number],
    ) -> "Vector":
        start_x, start_y = start_point
        end_x, end_y = end_point
        return cls(end_x - start_x, end_y - start_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)

        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: "Vector") -> int:
        first_length = self.get_length()
        second_length = vector.get_length()

        if first_length == 0 or second_length == 0:
            return 0

        dot_product = self.x * vector.x + self.y * vector.y
        cos_value = dot_product / (first_length * second_length)
        cos_value = max(-1.0, min(1.0, cos_value))

        angle = math.degrees(math.acos(cos_value))
        return int(round(angle))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_value = math.cos(radians)
        sin_value = math.sin(radians)

        new_x = self.x * cos_value - self.y * sin_value
        new_y = self.x * sin_value + self.y * cos_value
        return Vector(new_x, new_y)
