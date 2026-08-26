from __future__ import annotations
from typing import Callable
import math


def check_is_vector(func: Callable) -> Callable:
    def wrapper(self: Vector, other: Vector) -> TypeError | Callable:
        if not isinstance(other, Vector):
            raise TypeError(f"Can't add {type(other)} to Vector")
        return func(self, other)
    return wrapper


class Vector:
    @staticmethod
    def round_float(value: int | float) -> int | float:
        if isinstance(value, float):
            return round(value, 2)
        return value

    def __init__(self, x_value: int | float, y_value: int | float) -> None:
        self.x = self.round_float(x_value)
        self.y = self.round_float(y_value)

    @check_is_vector
    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    @check_is_vector
    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | float | int:
        if not isinstance(other, Vector):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> Vector:
        x1, y1 = start_point
        x2, y2 = end_point
        return cls(x2 - x1, y2 - y1)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        cos_angle = self * other / (self.get_length() * other.get_length())
        angle_radians = math.acos(cos_angle)
        return round(math.degrees(angle_radians))

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        modul_self = math.sqrt(self.x ** 2 + self.y ** 2)
        return round(
            math.degrees(
                math.acos(
                    (self * y_axis)
                    / modul_self
                )
            )
        )

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(
            self.x * math.cos(radians) - self.y * math.sin(radians),
            self.x * math.sin(radians) + self.y * math.cos(radians)
        )
