from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Union

Number = Union[int, float]


def _round2(value: Number) -> float:
    return round(float(value), 2)


@dataclass
class Vector:
    x: float
    y: float

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

        factor = float(other)
        return Vector(self.x * factor, self.y * factor)

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
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)

        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: "Vector") -> int:
        first_len = self.get_length()
        second_len = vector.get_length()
        if first_len == 0 or second_len == 0:
            return 0

        dot_product = self.x * vector.x + self.y * vector.y
        cos_a = dot_product / (first_len * second_len)
        cos_a = max(-1.0, min(1.0, cos_a))

        angle_deg = math.degrees(math.acos(cos_a))
        return int(round(angle_deg))

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_value = math.cos(radians)
        sin_value = math.sin(radians)

        rotated_x = self.x * cos_value - self.y * sin_value
        rotated_y = self.x * sin_value + self.y * cos_value
        return Vector(rotated_x, rotated_y)
