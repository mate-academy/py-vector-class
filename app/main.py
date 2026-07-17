from __future__ import annotations
import math
from typing import Union


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
        self,
        other: Union[int, float, Vector]
    ) -> Union[Vector, float]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

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
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        cos_theta = (self * other) / (
            self.get_length() * other.get_length()
        )
        cos_theta = max(-1.0, min(1.0, cos_theta))
        return round(math.degrees(math.acos(cos_theta)))

    def get_angle(self) -> int:
        cos_theta = self.y / self.get_length()
        cos_theta = max(-1.0, min(1.0, cos_theta))
        return round(math.degrees(math.acos(cos_theta)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_val = math.cos(radians)
        sin_val = math.sin(radians)
        x_prime = self.x * cos_val - self.y * sin_val
        y_prime = self.x * sin_val + self.y * cos_val
        return Vector(x_prime, y_prime)
