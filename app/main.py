from __future__ import annotations
from math import degrees, acos, radians, cos, sin


class Vector:
    def __init__(self, axis_x: float, axis_y: float) -> None:
        self.x = round(axis_x, 2)
        self.y = round(axis_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

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
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        return round(
            degrees(
                acos(self * other / (self.get_length() * other.get_length()))
            )
        )

    def get_angle(self) -> int:
        return round(degrees(acos(self * Vector(0, 1) / self.get_length())))

    def rotate(self, degree: int) -> Vector:
        rad = radians(degree)
        new_x = self.x * cos(rad) - self.y * sin(rad)
        new_y = self.x * sin(rad) + self.y * cos(rad)
        return Vector(new_x, new_y)
