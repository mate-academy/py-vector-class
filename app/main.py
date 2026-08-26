from __future__ import annotations
from math import sqrt, pow, degrees, acos, radians, cos, sin


class Vector:
    def __init__(self, x_coordinate: float,
                 y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> int | float | Vector:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        raise TypeError(f"unsupported operand type(s)"
                        f" for multiplication:  {type(other)}")

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self) -> Vector:
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other: float | int) -> float | int:
        return round(
            degrees(acos(
                self * other / (self.get_length() * other.get_length())))
        )

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, rotate: int) -> Vector:
        return Vector(
            cos(radians(rotate)) * self.x - sin(radians(rotate)) * self.y,
            sin(radians(rotate)) * self.x + cos(radians(rotate)) * self.y
        )
