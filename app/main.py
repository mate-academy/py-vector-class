from __future__ import annotations

import math
from types import NotImplementedType


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
        self,
        other: float | int | Vector,
    ) -> Vector | float | NotImplementedType:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float],
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> float:
        dot_product = self * other
        lengths_product = self.get_length() * other.get_length()

        if lengths_product == 0:
            return 0

        # Clamp the cosine value to the valid range [-1.0, 1.0]
        # to avoid float precision errors.
        cos_a = max(min(dot_product / lengths_product, 1.0), -1.0)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        # Angle between current vector and positive Y axis (0, 1)
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)

        # Standard 2D rotation matrix multiplication.
        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a

        return Vector(new_x, new_y)
