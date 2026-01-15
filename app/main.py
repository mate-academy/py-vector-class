from __future__ import annotations
import math


class Vector:

    def __init__(self, x_: int | float, y_: int | float) -> None:
        self.x = round(x_, 2)
        self.y = round(y_, 2)

    def __add__(self, other: Vector) -> Vector:
        x_sum = self.x + other.x
        y_sum = self.y + other.y
        return Vector(x_sum, y_sum)

    def __sub__(self, other: Vector) -> Vector:
        x_sub = self.x - other.x
        y_sub = self.y - other.y
        return Vector(x_sub, y_sub)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0], end_point[1]
                   - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        return round(
            math.degrees(
                math.acos(self.__mul__(other)
                          / (self.get_length()
                             * other.get_length()))))

    def get_angle(self) -> int:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: int) -> Vector:
        new_x = (self.x * math.cos(math.radians(degrees))
                 - self.y * math.sin(math.radians(degrees)))
        new_y = (self.x * math.sin(math.radians(degrees))
                 + self.y * math.cos(math.radians(degrees)))
        return Vector(new_x, new_y)
