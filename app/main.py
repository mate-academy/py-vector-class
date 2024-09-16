from __future__ import annotations
from math import sqrt, degrees, acos, radians, cos, sin


class Vector:
    def __init__(self, dot_x: float, dot_y: float) -> None:
        self.x = round(dot_x, 2)
        self.y = round(dot_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int) -> Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: float,
                                    end_point: float) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(degrees(acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = self.y / self.get_length()
        return round(degrees(acos(cos_a)))

    def rotate(self, degrees: int) -> Vector:
        theta = radians(degrees)
        new_x = (cos(theta) * self.x - sin(theta) * self.y)
        new_y = (sin(theta) * self.x + cos(theta) * self.y)
        return Vector(new_x, new_y)
