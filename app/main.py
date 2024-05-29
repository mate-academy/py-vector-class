from __future__ import annotations
from math import degrees, acos, radians, sin, cos


class Vector:
    def __init__(self, x_: int, y_: int) -> None:
        self.x = round(x_, 2)
        self.y = round(y_, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_=self.x + other.x,
            y_=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_=self.x - other.x,
            y_=self.y - other.y
        )

    def __mul__(self, other: float | int | Vector) -> Vector | float | int:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            x_=self.x * other,
            y_=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(
            x_=end_point[0] - start_point[0],
            y_=end_point[1] - start_point[1]
        )

    def get_length(self) -> float | int:
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(
            x_=self.x / length,
            y_=self.y / length
        )

    def angle_between(self, other: Vector) -> float | int:
        result = (self * other) / (self.get_length() * other.get_length())
        return round(degrees(acos(result)))

    def get_angle(self) -> float | int:
        positive_y = Vector(0, 1)
        result = ((self * positive_y)
                  / (self.get_length() * positive_y.get_length()))
        return round(degrees(acos(result)))

    def rotate(self, degree: int) -> Vector:
        return Vector(
            x_=self.x * cos(radians(degree)) - self.y * sin(radians(degree)),
            y_=self.x * sin(radians(degree)) + self.y * cos(radians(degree))
        )
