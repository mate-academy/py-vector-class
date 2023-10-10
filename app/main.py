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

    def __mul__(self, other: Vector or float) -> Vector:
        return (self.y * other.y + self.x * other.x
                if isinstance(other, Vector)
                else Vector(round(self.x * other, 2), round(self.y * other, 2))
                )

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return cls(
            vector_x=end[0] - start[0],
            vector_y=end[1] - start[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            round(self.x / Vector.get_length(self), 2),
            round(self.y / Vector.get_length(self), 2)
        )

    def angle_between(self, other: Vector) -> int:
        return round(
            math.degrees(
                math.acos(
                    Vector.__mul__(self, other)
                    / (Vector.get_length(self)
                       * Vector.get_length(other))
                )
            )
        )

    def get_angle(self) -> int:
        return Vector.angle_between(self, Vector(0, 10))

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            round(math.cos(math.radians(degrees)) * self.x
                  - math.sin(math.radians(degrees)) * self.y, 2),
            round(math.sin(math.radians(degrees)) * self.x
                  + math.cos(math.radians(degrees)) * self.y, 2)
        )
