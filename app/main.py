from __future__ import annotations
from math import acos, degrees, sin, cos, radians


class Vector:
    def __init__(self, x_cord: float, y_cord: float) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, multiplier: float | Vector) -> Vector | float:
        if isinstance(multiplier, (int, float)):
            return Vector(self.x * multiplier, self.y * multiplier)
        else:
            return self.x * multiplier.x + self.y * multiplier.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length != 0:
            return Vector(self.x / length, self.y / length)
        else:
            return Vector(0, 0)

    def angle_between(self, other: Vector) -> int:
        multiply = self.x * other.x + self.y * other.y
        return round(
            degrees(acos(multiply / (self.get_length() * other.get_length())))
        )

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 10))

    def rotate(self, degree: int) -> Vector:
        return Vector(cos(radians(degree)) * self.x
                      - sin(radians(degree)) * self.y,
                      sin(radians(degree)) * self.x
                      + cos(radians(degree)) * self.y)
