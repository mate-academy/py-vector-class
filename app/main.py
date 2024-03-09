from __future__ import annotations
import math


class Vector:
    def __init__(self, x_: float, y_: float) -> None:
        self.x = round(x_, 2)
        self.y = round(y_, 2)

    def __add__(self, second: Vector) -> Vector:
        return Vector(self.x + second.x,
                      self.y + second.y)

    def __sub__(self, second: Vector) -> Vector:
        return Vector(self.x - second.x,
                      self.y - second.y)

    def __mul__(self, second: Vector | int | float) -> Vector | int | float:
        if isinstance(second, Vector):
            return self.x * second.x + self.y * second.y
        return Vector(self.x * second, self.y * second)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        # in case of n-space
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

    def rotate(self, degrees: int) -> Vector:
        # x2 = cosβx1−sinβy1 y2 = sinβx1 + cosβy1
        return Vector(math.cos(math.radians(degrees)) * self.x
                      - math.sin(math.radians(degrees)) * self.y,

                      math.sin(math.radians(degrees)) * self.x
                      + math.cos(math.radians(degrees)) * self.y
                      )
