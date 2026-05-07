from __future__ import division
from __future__ import annotations
from typing import Union
import math


class Vector:
    def __init__(self, axis_x: float, axis_y: float) -> None:
        self.x = round(axis_x, 2)
        self.y = round(axis_y, 2)

    def __str__(self) -> str:
        return f"{self.x, self.y}"

    def __repr__(self) -> str:
        return f"Vector{self.x, self.y}"

    def __add__(self, other: Union[Vector]) -> "Vector":
        if isinstance(other, Vector):
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Vector(new_x, new_y)
        else:
            return NotImplemented

    def __sub__(self, other: Union[Vector]) -> "Vector":
        if isinstance(other, Vector):
            new_x = self.x - other.x
            new_y = self.y - other.y
            return Vector(new_x, new_y)
        else:
            return NotImplemented

    def __mul__(self, other: Union[Vector, int, float]) \
            -> Union[float, Vector]:
        if isinstance(other, Vector):
            new_x = self.x * other.x
            new_y = self.y * other.y
            return new_x + new_y
        elif isinstance(other, (int, float)):
            new_x = self.x * other
            new_y = self.y * other
            return Vector(new_x, new_y)
        else:
            return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[float, float],
                                    end_point: tuple[float, float]) \
            -> "Vector":
        start_x, start_y = start_point
        end_x, end_y = end_point
        new_x = end_x - start_x
        new_y = end_y - start_y
        return cls(new_x, new_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        lenght = self.get_length()
        if lenght == 0.0:
            return Vector(0, 0)
        new_x = self.x / self.get_length()
        new_y = self.y / self.get_length()
        return Vector(new_x, new_y)

    def angle_between(self, vector: "Vector") -> int:
        length_self = self.get_length()
        length_other = vector.get_length()
        if length_self == 0.0 or length_other == 0.0:
            return 0
        if isinstance(vector, Vector):
            dot_product = self * vector
            cos_theta = dot_product / (length_self * length_other)
            cos_theta = round(cos_theta, 10)
            angle_radians = math.acos(cos_theta)
            return round(math.degrees(angle_radians))
        else:
            return NotImplemented

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> "Vector":
        readian_ver = math.radians(degrees)
        new_x = ((self. x * math.cos(readian_ver))
                 - (self. y * math.sin(readian_ver)))
        new_y = ((self. x * math.sin(readian_ver))
                 + (self. y * math.cos(readian_ver)))
        return Vector(new_x, new_y)