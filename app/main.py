from __future__ import annotations

import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other: float | Vector) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            x=round(self.x * other, 2),
            y=round(self.y * other, 2),
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def get_normalized(self) -> Vector:
        return Vector(
            x=round(self.x / self.get_length(), 2),
            y=round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other: Vector) -> int:
        angle_betw = (self * other
                      / (self.get_length()
                         * other.get_length()))
        return round(math.degrees(math.acos(angle_betw)))

    def get_angle(self) -> int:
        angle_cos = self.y / self.get_length()
        return round(math.degrees(math.acos(angle_cos)))

    def rotate(self, degrees: int) -> Vector:
        degrees = math.radians(degrees)
        rotate_matrix = [
            [math.cos(degrees), -math.sin(degrees)],
            [math.sin(degrees), math.cos(degrees)],
        ]
        return Vector(
            x=rotate_matrix[0][0] * self.x + rotate_matrix[0][1] * self.y,
            y=rotate_matrix[1][0] * self.x + rotate_matrix[1][1] * self.y,
        )
