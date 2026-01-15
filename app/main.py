from __future__ import annotations
from typing import Union
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:  # noqa: VNE001
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

    def __mul__(self, other: Union[int, float, Vector]) \
            -> Union[int, float, Vector]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(
                x=self.x * other,
                y=self.y * other
            )

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) \
            -> Vector:
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self) -> Union[int, float]:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(
            x=self.x / length,
            y=self.y / length
        )

    def angle_between(self, other: Vector) -> int:
        dot = self * other
        len1 = self.get_length()
        len2 = other.get_length()
        cos_angle = dot / (len1 * len2)
        angle_rad = math.acos(cos_angle)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def get_angle(self) -> Union[int, float]:
        y_vector = Vector(0, 1)
        return self.angle_between(y_vector)

    def rotate(self, degrees: Union[int, float]) -> Vector:
        degrees = math.radians(degrees)
        new_x = self.x * math.cos(degrees) - self.y * math.sin(degrees)
        new_y = self.x * math.sin(degrees) + self.y * math.cos(degrees)
        return Vector(
            x=new_x,
            y=new_y
        )
