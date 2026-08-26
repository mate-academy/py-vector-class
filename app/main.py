from __future__ import annotations
from math import sqrt
import math


class Vector:

    def __init__(self, x_: float, y_: float) -> None:
        self.x = round(x_, 2)
        self.y = round(y_, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                x_=self.x + other.x,
                y_=self.y + other.y
            )

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                x_=self.x - other.x,
                y_=self.y - other.y
            )

    def __mul__(self, other: Vector | float | int) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(self.x * other,
                      self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> Vector:
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]
        return Vector(new_x, new_y)

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length_vector = self.get_length()
        lenx = self.x / length_vector
        leny = self.y / length_vector
        return Vector(x_=lenx, y_=leny)

    def angle_between(self, other: Vector) -> int:
        top = self.x * other.x + self.y * other.y
        bot = self.get_length() * other.get_length()
        result = top / bot
        return round(math.degrees(math.acos(result)))

    def get_angle(self, my_x: int = 0, my_y: int = 1) -> int:
        top = self.x * my_x + self.y * my_y
        bot = self.get_length() * 1
        result = top / bot
        return round(math.degrees(math.acos(result)))

    def rotate(self, other: int) -> Vector:
        radians = math.radians(other)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(x_=new_x, y_=new_y)
