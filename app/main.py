from __future__ import annotations
from math import degrees, acos, sin, cos, radians


class Vector:
    def __init__(self, x_coordinate: float | int,
                 y_coordinate: float | int) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

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

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(
            self.x * other,
            self.y * other
        )

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()

        )

    def angle_between(self, other: Vector) -> int | float:
        return round(degrees(acos(self.__mul__(other)
                                  / (self.get_length() * other.get_length()))))

    def get_angle(self) -> int | float:
        return round(degrees(acos(self.y / self.get_length())), 0)

    def rotate(self, degree: int) -> Vector:
        return Vector(
            self.x * cos(radians(degree)) - self.y * sin(radians(degree)),
            self.x * sin(radians(degree)) + self.y * cos(radians(degree))

        )
