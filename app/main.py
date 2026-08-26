from __future__ import annotations
import math


class Vector:
    def __init__(self, x_: int | float, y_: int | float) -> None:
        x_ = round(x_, 2)
        y_ = round(y_, 2)
        self.x = x_
        self.y = y_

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | int | float:
        if isinstance(other, int | float):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def get_normalized(self) -> Vector:
        inv_vector_len = 1 / self.get_length()
        return Vector(self.x * inv_vector_len, self.y * inv_vector_len)

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        rotated_x = math.cos(radians) * self.x - math.sin(radians) * self.y
        rotated_y = math.cos(radians) * self.y + math.sin(radians) * self.x
        return Vector(rotated_x, rotated_y)
