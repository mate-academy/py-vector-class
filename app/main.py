from __future__ import annotations
import math


class Vector:

    def __init__(self, x_co: float, y_co: float) -> None:
        self.x = round(x_co, 2)
        self.y = round(y_co, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple) -> Vector:
        return (cls(end_point[0], end_point[1])
                - cls(start_point[0], start_point[1]))

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )

    def angle_between(self, vector: Vector) -> int:
        return round(
            math.degrees(
                math.acos(
                    (self * vector) / (self.get_length() * vector.get_length())
                )
            )
        )

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            self.x * math.cos(math.radians(degrees)) - (
                self.y * math.sin(math.radians(degrees))
            ),
            self.x * math.sin(math.radians(degrees)) + (
                self.y * math.cos(math.radians(degrees))
            )
        )
