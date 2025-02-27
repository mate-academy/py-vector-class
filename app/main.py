from __future__ import annotations

import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x=self.x - other.x, y=self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | float | int:
        if isinstance(other, (int, float)):
            return Vector(x=self.x * other, y=self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[int, int],
            end_point: tuple[int, int]
    ) -> Vector:
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float | int:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(x=self.x / length, y=self.y / length)

    def angle_between(self, other: Vector) -> int:
        return round(math.degrees(math.acos(
            (self * other) / (self.get_length() * other.get_length())
        )))

    def get_angle(self) -> int:
        return self.angle_between(Vector(x=0, y=1))

    def rotate(self, degrees: int) -> Vector:
        radian = math.radians(degrees)
        return Vector(
            x=self.x * math.cos(radian) - self.y * math.sin(radian),
            y=self.x * math.sin(radian) + self.y * math.cos(radian)
        )
