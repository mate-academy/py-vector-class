from __future__ import annotations
from math import sqrt, acos, degrees, ceil, atan, cos, sin, radians


class Vector:
    def __init__(self, x_coord: float , y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

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

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return (self.x * other.x + self.y * other.y)
        return Vector(
            round(self.x * other, 2),
            round(self.y * other, 2)
        )

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> classmethod:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, vector: Vector) -> int | float:
        return ceil(degrees(acos(
            self.__mul__(vector) / (self.get_length() * vector.get_length()))
        ))

    def get_angle(self) -> int | float:
        if self.y < 0:
            return 180 - abs(ceil(degrees(atan(self.x / self.y))))
        return abs(ceil(degrees(atan(self.x / self.y))))

    def rotate(self, degree: int) -> Vector:
        return Vector(
            round((cos(radians(degree)) * self.x)
                  - (sin(radians(degree)) * self.y), 2),
            round((sin(radians(degree)) * self.x)
                  + (cos(radians(degree)) * self.y), 2)
        )
