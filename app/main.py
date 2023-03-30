from __future__ import annotations
from typing import Union
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other: Union[Vector, float]) -> Union[Vector, float]:
        if isinstance(other, (float, int)):
            return Vector(
                x=self.x * other,
                y=self.y * other
            )
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> Vector:
        return Vector(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        len_of_not_norm_vector = Vector.get_length(self)
        return Vector(
            x=self.x / len_of_not_norm_vector,
            y=self.y / len_of_not_norm_vector
        )

    def angle_between(self, second_vector: Vector) -> int:
        return round(
            math.degrees(
                math.acos(
                    self * second_vector /
                    self.get_length() * second_vector.get_length()
                )
            )
        )

    def get_angle(self) -> int:
        second_vector = Vector(x=0, y=1)
        return self.angle_between(second_vector)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(
            x=math.cos(radians) * self.x - math.sin(radians) * self.y,
            y=math.sin(radians) * self.x + math.cos(radians) * self.y
        )
