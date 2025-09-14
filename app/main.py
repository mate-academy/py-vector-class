from __future__ import annotations

import math
from typing import Union, Tuple


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x: float = round(x_coord, 2)
        self.y: float = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[Vector, float]) -> Union[Vector, float]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

        raise TypeError(
            f"Unsupported operand for *: 'Vector' and '{type(other).__name__}'"
        )

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: Tuple[float, float],
        end_point: Tuple[float, float],
    ) -> Vector:
        delta_x = end_point[0] - start_point[0]
        delta_y = end_point[1] - start_point[1]
        return cls(delta_x, delta_y)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0.0, 0.0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        len_self = self.get_length()
        len_other = other.get_length()
        if len_self == 0 or len_other == 0:
            return 0

        cos_angle = (self.x * other.x + self.y * other.y) / (
            len_self * len_other
        )
        cos_angle = max(min(cos_angle, 1.0), -1.0)
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            return 0

        cos_angle = self.y / length
        cos_angle = max(min(cos_angle, 1.0), -1.0)
        return round(math.degrees(math.acos(cos_angle)))

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        x_rotated = self.x * cos_theta - self.y * sin_theta
        y_rotated = self.x * sin_theta + self.y * cos_theta
        return Vector(x_rotated, y_rotated)
