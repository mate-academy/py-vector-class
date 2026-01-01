from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Union

Number = Union[int, float]


def _r2(value: Number) -> float:
    return round(float(value), 2)


@dataclass
class Vector:
    x: float
    y: float

    def __init__(self, x: Number, y: Number) -> None:
        self.x = _r2(x)
        self.y = _r2(y)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union["Vector", Number]) -> Union["Vector", float]:
        if isinstance(other, Vector):
            # dot product (NO rounding)
            return self.x * other.x + self.y * other.y
        # multiply by number -> Vector (coords rounded in __init__)
        return Vector(self.x * float(other), self.y * float(other))

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[Number, Number],
        end_point: tuple[Number, Number],
    ) -> "Vector":
        sx, sy = start_point
        ex, ey = end_point
        return cls(ex - sx, ey - sy)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: "Vector") -> int:
        a_len = self.get_length()
        b_len = vector.get_length()
        if a_len == 0 or b_len == 0:
            return 0

        dot = self.x * vector.x + self.y * vector.y
        cos_a = dot / (a_len * b_len)

        # clamp to [-1, 1] to avoid acos domain errors from float noise
        cos_a = max(-1.0, min(1.0, cos_a))

        degrees = math.degrees(math.acos(cos_a))
        return int(round(degrees))

    def get_angle(self) -> int:
        # angle between vector and positive Y axis
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> "Vector":
        rad = math.radians(degrees)
        cos_t = math.cos(rad)
        sin_t = math.sin(rad)

        # standard rotation around origin
        new_x = self.x * cos_t - self.y * sin_t
        new_y = self.x * sin_t + self.y * cos_t
        return Vector(new_x, new_y)
