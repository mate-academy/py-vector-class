from __future__ import annotations
from typing import Union
import math

Number = Union[int, float]


class Vector:
    def __init__(self, x: Number, y: Number) -> None:
        self.x: float = round(x, 2)
        self.y: float = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[Number, Vector]) -> Union[float, Vector]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[Number, Number],
            end_point: tuple[Number, Number],
    ) -> Vector:
        sx, sy = start_point
        ex, ey = end_point
        return cls(ex - sx, ey - sy)

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector (0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        len1 = self.get_length()
        len2 = other.get_length()
        if len1 == 0 or len2 == 0:
            raise ValueError("Cannot compute angle with zero-length vector")

        cos_a = (self * other) / (len1 * len2)

        cos_a = max(-1.0, min(1.0, cos_a))
        angle_deg = math.degrees(math.acos(cos_a))
        return round(angle_deg)

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot compute angle of zero-length vector")

        cos_a = self.y / length  # angle with positive Y axis

        cos_a = max(-1.0, min(1.0, cos_a))
        angle_deg = math.degrees(math.acos(cos_a))
        return round(angle_deg)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        x_new = self.x * cos_a - self.y * sin_a
        y_new = self.x * sin_a + self.y * cos_a
        return Vector(x_new, y_new)
