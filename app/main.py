from __future__ import annotations
import math


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y,
        )

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(
                x=round(self.x * other, 2),
                y=round(self.y * other, 2),
            )
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()

        if length == 0:
            return Vector(0, 0)

        return Vector(x=round(self.x / length, 2), y=round(self.y / length, 2))

    def angle_between(self, other: Vector) -> int:
        cos_angle = (self * other) / (self.get_length() * other.get_length())
        cos_angle = max(-1.0, min(1.0, cos_angle))
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        cos_angle = math.cos(math.radians(degrees))
        sin_angle = math.sin(math.radians(degrees))

        x = round((self.x * cos_angle) - (self.y * sin_angle), 2)
        y = round((self.x * sin_angle) + (self.y * cos_angle), 2)

        return Vector(x, y)
