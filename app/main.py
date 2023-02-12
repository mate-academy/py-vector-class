from __future__ import annotations
from math import sqrt, degrees, acos, fabs, cos, sin, radians


class Vector:
    def __init__(self, coordinate1: float, coordinate2: float) -> None:
        self.x = round(coordinate1, 2)
        self.y = round(coordinate2, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(degrees(acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, fabs(self.y)))

    def rotate(self, degrees: int) -> Vector:
        return Vector(self.x * cos(radians(degrees))
                      - self.y * sin(radians(degrees)),
                      self.y * cos(radians(degrees))
                      + self.x * sin(radians(degrees)))
