from __future__ import annotations
import math


class Vector:
    def __init__(self, x_: float, y_: float) -> None:
        self.x = round(x_, 2)
        self.y = round(y_, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(*[end_point[i] - start_point[i]
                     for i in range(len(start_point))])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        len = self.get_length()
        return Vector(self.x / len,
                      self.y / len)

    def angle_between(self, second: Vector) -> float:
        return round(math.degrees(math.acos(self * second
                     / (self.get_length() * second.get_length()))), 0)

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degree: int) -> Vector:
        return Vector(math.cos(math.radians(degree)) * self.x
                      - math.sin(math.radians(degree)) * self.y,
                      math.sin(math.radians(degree)) * self.x
                      + math.cos(math.radians(degree)) * self.y
                      )
