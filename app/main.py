from __future__ import annotations
import math


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        self.x = round(self.x + other.x, 2)
        self.y = round(self.y + other.y, 2)
        return self

    def __sub__(self, other: Vector) -> Vector:
        self.x = round(self.x - other.x, 2)
        self.y = round(self.y - other.y, 2)
        return self

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, float | int):
            self.x *= other
            self.y *= other
            return Vector(round(self.x, 2), round(self.y, 2))
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @staticmethod
    def create_vector_by_two_points(
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def get_normalized(self) -> Vector:
        new_x = self.x / (
            self.x ** 2 + self.y ** 2
        ) ** (1 / 2)
        new_y = self.y / (
            self.x ** 2 + self.y ** 2
        ) ** (1 / 2)
        return Vector(round(new_x, 2), round(new_y, 2))

    def angle_between(self, other: Vector) -> int:
        cos_angle = (
            self.x * other.x + self.y * other.y
        ) / (
            ((self.x ** 2 + self.y ** 2) ** (1 / 2))
            * ((other.x ** 2 + other.y ** 2) ** (1 / 2))
        )
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        cos_angle = self.y / (
            ((self.x ** 2 + self.y ** 2) ** (1 / 2))
        )
        return round(math.degrees(math.acos(cos_angle)))

    def rotate(self, angle: int) -> Vector:
        new_x = self.x * math.cos(
            math.radians(angle)
        ) - self.y * math.sin(
            math.radians(angle)
        )
        new_y = self.x * math.sin(
            math.radians(angle)
        ) + self.y * math.cos(
            math.radians(angle)
        )
        return Vector(round(new_x, 2), round(new_y, 2))
