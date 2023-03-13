from __future__ import annotations
import math
from typing import Union, Any


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x_coord = round(x_coord, 2)
        self.y_coord = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        x_coord = self.x_coord + other.x_coord
        y_coord = self.y_coord + other.y_coord
        return Vector(x_coord=x_coord, y_coord=y_coord)

    def __sub__(self, other: Vector) -> Vector:
        x_coord = self.x_coord - other.x_coord
        y_coord = self.y_coord - other.y_coord
        return Vector(x_coord=x_coord, y_coord=y_coord)

    def __mul__(self, other: Union[int, float, Vector]) -> Any:
        if isinstance(other, Vector):
            dot_product = self.x_coord * other.x_coord \
                + self.y_coord * other.y_coord
            return dot_product
        x_coord = self.x_coord * other
        y_coord = self.y_coord * other
        return Vector(x_coord=x_coord, y_coord=y_coord)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple)\
            -> Vector:
        x_coord = end_point[0] - start_point[0]
        y_coord = end_point[1] - start_point[1]
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return math.sqrt(pow(self.x_coord, 2) + pow(self.y_coord, 2))

    def get_normalized(self) -> Vector:
        length = self.get_length()
        x_coord = round(self.x_coord / length, 2)
        y_coord = round(self.y_coord / length, 2)
        return Vector(x_coord=x_coord, y_coord=y_coord)

    def angle_between(self, other: Vector) -> int:
        cos_a = self.__mul__(other) / self.get_length() / other.get_length()
        return int(round(math.degrees(math.acos(cos_a)), 0))

    def get_angle(self) -> int:
        y_coord = abs(self.y_coord)
        other = Vector(x_coord=0, y_coord=y_coord)
        return self.angle_between(other)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x_coord = round(self.x_coord * math.cos(radians)
                        - self.y_coord * math.sin(radians), 2)
        y_coord = round(self.x_coord * math.sin(radians)
                        + self.y_coord * math.cos(radians), 2)
        return Vector(x_coord=x_coord, y_coord=y_coord)
