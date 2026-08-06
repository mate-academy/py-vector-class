from __future__ import annotations
from typing import Union, Tuple
import math


class Vector:

    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> "Vector":
        return Vector(
            x_coord=self.x + other.x,
            y_coord=self.y + other.y
        )

    def __sub__(self, other: Vector) -> "Vector":
        return Vector(
            x_coord=self.x - other.x,
            y_coord=self.y - other.y
        )

    def __mul__(self, other: Union[Vector, float]) -> Union["Vector", float]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            x_coord=self.x * other,
            y_coord=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: Tuple,
                                    end_point: Tuple) -> "Vector":
        return Vector(
            x_coord=end_point[0] - start_point[0],
            y_coord=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        inv_length = 1 / self.get_length()
        return Vector(
            x_coord=self.x * inv_length,
            y_coord=self.y * inv_length
        )

    def angle_between(self, other: Vector) -> int:
        cos_a = ((self.x * other.x
                  + self.y * other.y)
                 / (self.get_length() * other.get_length()))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> "Vector":
        return Vector(
            x_coord=(self.x * math.cos(math.radians(degrees))
                     - self.y * math.sin(math.radians(degrees))),
            y_coord=(self.x * math.sin(math.radians(degrees))
                     + self.y * math.cos(math.radians(degrees)))
        )
