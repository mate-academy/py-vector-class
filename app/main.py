from __future__ import annotations
import math


class Vector:

    def __init__(self, coord_x: int | float, coord_y: int | float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:

        start_x, start_y = start_point
        end_x, end_y = end_point
        return cls(end_x - start_x, end_y - start_y)

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / Vector.get_length(self), self.y / Vector.get_length(self)
        )

    def angle_between(self, other: Vector) -> float:
        cos_a = (self * other) / (Vector.get_length(self)
                                  * Vector.get_length(other))
        return round(math.degrees(math.acos(cos_a)), 0)

    def get_angle(self) -> int | float:
        return Vector.angle_between(self, Vector(0, 1))

    def rotate(self, degrees: int | float) -> Vector:
        radians = math.radians(degrees)
        return Vector(
            math.cos(radians) * self.x - math.sin(radians) * self.y,
            math.sin(radians) * self.x + math.cos(radians) * self.y
        )
