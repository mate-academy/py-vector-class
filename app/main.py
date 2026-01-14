from __future__ import annotations
import math


class Vector:
    def __init__(self, coord_x: int | float, coord_y: int | float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            coord_x=round((self.x + other.x), 2),
            coord_y=round((self.y + other.y), 2)
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            coord_x=round((self.x - other.x), 2),
            coord_y=round((self.y - other.y), 2)
        )

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(
            coord_x=round(self.x * other, 2),
            coord_y=round(self.y * other, 2)
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:

        x1, y1 = start_point
        x2, y2 = end_point
        return cls(
            coord_x=round((x2 - x1), 2),
            coord_y=round((y2 - y1), 2)
        )

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            coord_x=round(self.x / self.get_length(), 2),
            coord_y=round(self.y / self.get_length(), 2)
        )

    def angle_between(self, vector: Vector) -> int:
        return round(
            math.degrees(
                math.acos(
                    self * vector
                    / (self.get_length() * vector.get_length())
                )
            )
        )

    def get_angle(self) -> int:
        cos = self.y / (self.get_length() * 1)
        return round(math.degrees(math.acos(cos)))

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            coord_x=round((math.cos(math.radians(degrees)) * self.x
                           - math.sin(math.radians(degrees)) * self.y), 2),
            coord_y=round((math.sin(math.radians(degrees)) * self.x
                           + math.cos(math.radians(degrees)) * self.y), 2)
        )
