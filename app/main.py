from __future__ import annotations
import math
from typing import Union, Tuple


class Vector:
    def __init__(self, xy: float, yy: float) -> None:
        self.xy = round(xy, 2)
        self.yy = round(yy, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.xy + other.xy, self.yy + other.yy)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.xy - other.xy, self.yy - other.yy)

    def __mul__(self, other: Union[int, float, Vector])\
            -> Union[Vector, float]:
        if isinstance(other, (int, float)):
            return Vector(self.xy * other, self.yy * other)
        elif isinstance(other, Vector):
            return self.xy * other.xy + self.yy * other.yy

    @classmethod
    def create_vector_by_two_points(cls, start_point: Tuple[float, float],
                                    end_point: Tuple[float, float]) -> Vector:
        xy = end_point[0] - start_point[0]
        yy = end_point[1] - start_point[1]
        return cls(xy, yy)

    def get_length(self) -> float:
        return math.sqrt(self.xy ** 2 + self.yy ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.xy / length, self.yy / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        length1 = self.get_length()
        length2 = other.get_length()
        cos_a = dot_product / (length1 * length2)
        angle_rad = math.degrees(math.acos(cos_a))
        return round(angle_rad)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        new_x = self.xy * cos_a - self.yy * sin_a
        new_y = self.xy * sin_a + self.yy * cos_a
        return Vector(new_x, new_y)
