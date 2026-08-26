from __future__ import annotations
import math


class Vector:

    def __init__(self, vector_x: float, vector_y: float) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: Vector) -> float | Vector:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        elif isinstance(other, (int, float)):
            return Vector(
                round(self.x * other, 2),
                round(self.y * other, 2)
            )

    @staticmethod
    def create_vector_by_two_points(
            start_point: tuple, end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        self.x = self.x / length
        self.y = self.y / length
        return Vector(self.x, self.y)

    def angle_between(self, other: Vector) -> int:
        return round(math.degrees(
            math.acos(
                (self * other) / (self.get_length() * other.get_length())
            )
        ))

    def get_angle(self) -> int:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degree: int | float) -> Vector:
        return Vector(
            self.x * math.cos(math.radians(degree))
            - self.y * math.sin(math.radians(degree)),
            self.x * math.sin(math.radians(degree))
            + self.y * math.cos(math.radians(degree))
        )
