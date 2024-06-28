from __future__ import annotations
from typing import Union
import math


class Vector:
    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Union[float, Vector]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_angle(self) -> int:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def angle_between(self, other: Vector) -> int:
        return round(math.degrees(math.acos(self.__mul__(other)
                                            / (self.get_length()
                                            * other.get_length()))))

    def rotate(self, degrees: int) -> Vector:
        angle_in_radians = math.radians(degrees)

        new_x = (self.x * math.cos(angle_in_radians)
                 - self.y * math.sin(angle_in_radians))
        new_y = (self.y * math.cos(angle_in_radians)
                 + self.x * math.sin(angle_in_radians))
        return Vector(new_x, new_y)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())
