from __future__ import annotations
from math import degrees, acos, radians, sin, cos


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                coord_x=self.x + other.x,
                coord_y=self.y + other.y,
            )

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                coord_x=self.x - other.x,
                coord_y=self.y - other.y,
            )

    def __mul__(self, other: int | float | Vector) -> Vector | int | float:
        if isinstance(other, (int, float)):
            return Vector(
                coord_x=round(self.x * other, 2),
                coord_y=round(self.y * other, 2),
            )
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            coord_x=end_point[0] - start_point[0],
            coord_y=end_point[1] - start_point[1],
        )

    def get_length(self) -> int | float:
        return (self.x**2 + self.y**2)**(1 / 2)

    def get_normalized(self) -> Vector:
        return Vector(
            coord_x=self.x / self.get_length(),
            coord_y=self.y / self.get_length(),
        )

    def angle_between(self, other: Vector) -> int | float:
        return round(
            degrees
            (acos(
                (self * other / (self.get_length() * other.get_length()))
            )
            )
        )

    def get_angle(self) -> int | float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        rad = radians(degrees)
        return Vector(
            coord_x=self.x * cos(rad) - self.y * sin(rad),
            coord_y=self.x * sin(rad) + self.y * cos(rad),
        )
