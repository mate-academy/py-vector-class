from __future__ import annotations

import math
from numbers import Real


class Vector:
    def __init__(self, x_coordinate: Real, y_coordinate: Real) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Real | "Vector") -> Real | "Vector":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, Real):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple[Real, Real], end_point: tuple[Real, Real]
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: "Vector") -> int:
        if not isinstance(vector, Vector):
            raise TypeError("angle_between expects a Vector")
        denominator = self.get_length() * vector.get_length()
        if denominator == 0:
            raise ValueError("Angle is undefined for a zero vector")
        cosine = (self.x * vector.x + self.y * vector.y) / denominator
        cosine = max(-1.0, min(1.0, cosine))
        return round(math.degrees(math.acos(cosine)))

    def get_angle(self) -> int:
        if self.get_length() == 0:
            raise ValueError("Angle is undefined for a zero vector")
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cosine = math.cos(radians)
        sine = math.sin(radians)
        return Vector(
            self.x * cosine - self.y * sine,
            self.x * sine + self.y * cosine,
        )
