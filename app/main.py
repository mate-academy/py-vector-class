from __future__ import annotations
from typing import Union, Tuple
import math


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(coord_x=round(self.x + other.x, 2),
                      coord_y=round(self.y + other.y, 2))

    def __sub__(self,
                other: Vector) -> Vector:
        return Vector(coord_x=round(self.x - other.x, 2),
                      coord_y=round(self.y - other.y, 2))

    def __mul__(self, other: Union[int,
                float, Vector]) -> Union[Vector, float]:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: Tuple[float, float],
                                    end_point: Tuple[float, float]) -> Vector:
        coord_x = end_point[0] - start_point[0]
        coord_y = end_point[1] - start_point[1]
        return cls(round(coord_x, 2), round(coord_y, 2))

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        coord_x = self.x / self.get_length()
        coord_y = self.y / self.get_length()
        return Vector(round(coord_x, 2), round(coord_y, 2))

    def angle_between(self, other_vector: Vector) -> float:
        cos_a = self.__mul__(other_vector) / (self.get_length()
                                              * other_vector.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: float) -> Vector:
        radian = math.radians(degrees)
        new_x = self.x * math.cos(radian) - self.y * math.sin(radian)
        new_y = self.x * math.sin(radian) + self.y * math.cos(radian)
        return Vector(new_x, new_y)
