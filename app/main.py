from __future__ import annotations
from typing import Union
import math


class Vector:
    def __init__(
            self,
            cord_x: Union[int, float],
            cord_y: Union[int, float]
    ) -> None:
        self.x = round(cord_x, 2)
        self.y = round(cord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float | int:
        if type(other) is Vector:
            return self.x * other.x + self.y * other.y
        else:
            return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple,
            end_point: tuple
    ) -> Vector:
        vector = (
            Vector(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])
        )
        return vector

    def get_length(self) -> int | float:
        # |a| = √ax2 + ay2
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        invlength = 1 / self.get_length()
        return Vector(self.x * invlength, self.y * invlength)

    def get_angle(self) -> int | int:
        return self.angle_between(Vector(0, 5))

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(
            self.x * math.cos(radians) - self.y * math.sin(radians),
            self.x * math.sin(radians) + self.y * math.cos(radians)
        )
