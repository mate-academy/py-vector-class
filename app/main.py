from __future__ import annotations
import math


class Vector:
    def __init__(self, point_x: int | float, point_y: int | float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

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

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            scalar = (
                self.x * other.x
                + self.y * other.y
            )
            return scalar
        return Vector(
            self.x * other,
            self.y * other
        )

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
        return math.sqrt(
            self.x ** 2
            + self.y ** 2
        )

    def get_normalized(self) -> Vector:
        inv_length = 1 / self.get_length()
        return Vector(
            self.x * inv_length,
            self.y * inv_length
        )

    def angle_between(self, other: Vector) -> float:
        cos_angle = self.__mul__(other) / (
            self.get_length()
            * other.get_length()
        )
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        cos_y = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_y)))

    def rotate(self, angel: int) -> Vector:
        return Vector(
            round(math.cos(math.radians(angel)) * self.x
                  - math.sin(math.radians(angel)) * self.y, 2),
            round(math.sin(math.radians(angel)) * self.x
                  + math.cos(math.radians(angel)) * self.y, 2)
        )
