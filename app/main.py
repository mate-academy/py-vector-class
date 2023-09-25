from __future__ import annotations
from typing import Union
import math


class Vector:

    def __init__(self, x_axis: float, y_axis: float) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, other: Vector) -> Vector:
        result = Vector(self.x + other.x, self.y + other.y)
        return result

    def __sub__(self, other: Vector) -> Vector:
        result = Vector(self.x - other.x, self.y - other.y)
        return result

    def __mul__(self, other: Union[Vector, int, float]
                ) -> Union[Vector, float, int]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        x1, y1 = start_point
        x2, y2 = end_point

        return cls(x2 - x1, y2 - y1)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int | float:
        return round(math.degrees(math.acos((self * other)
                                            / (self.get_length()
                                               * other.get_length()))))

    def get_angle(self) -> float:
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: float) -> Vector:
        radian = math.radians(degrees)
        new_x = self.x * math.cos(radian) - self.y * math.sin(radian)
        new_y = self.x * math.sin(radian) + self.y * math.cos(radian)
        return Vector(new_x, new_y)
