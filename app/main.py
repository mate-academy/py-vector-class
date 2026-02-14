from __future__ import annotations
from typing import Union
import math


class Vector:
    def __init__(self, x : float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[float, int, Vector]) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other,
                          self.y * other)
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[float, float],
                                    end_point: tuple[float, float]) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ZeroDivisionError("Cannot normalize zero vector.")
        return Vector(self.x / length,
                      self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot = self * other
        len_1 = self.get_length()
        len_2 = other.get_length()
        if len_1 == 0 or len_2 == 0:
            raise ZeroDivisionError("Angle with zero vector is undefined.")
        cos_a = dot / (len_1 * len_2)
        cos_a = max(-1.0, min(1.0, cos_a))

        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self) -> int:
        length = self.get_length()

        if length == 0:
            return 0
        cos_a = self.y / length
        cos_a = max(-1.0, min(1.0, cos_a))

        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_radians = math.cos(radians)
        sin_radians = math.sin(radians)

        return Vector(self.x * cos_radians - self.y * sin_radians,
                      self.x * sin_radians + self.y * cos_radians)
    