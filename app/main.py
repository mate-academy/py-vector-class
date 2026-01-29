from __future__ import annotations
import math
from typing import Union, Tuple


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x_coord: float = round(x_coord, 2)
        self.y_coord: float = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x_coord + other.x_coord, self.y_coord + other.y_coord
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x_coord - other.x_coord, self.y_coord - other.y_coord
        )

    def __mul__(
            self,
            other: Union[Vector, float, int]
    ) -> Union[Vector, float]:
        if isinstance(other, Vector):
            return self.x_coord * other.x_coord + self.y_coord * other.y_coord
        elif isinstance(other, (int, float)):
            return Vector(self.x_coord * other, self.y_coord * other)
        else:
            raise TypeError("Multiplication supports only Vector or number")

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: Tuple[float, float],
            end_point: Tuple[float, float]
    ) -> Vector:
        x_coord = end_point[0] - start_point[0]
        y_coord = end_point[1] - start_point[1]
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return math.sqrt(self.x_coord ** 2 + self.y_coord ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x_coord / length, self.y_coord / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        lengths_product = self.get_length() * other.get_length()

        if lengths_product == 0:
            return 0

        cos_a = dot_product / lengths_product

        cos_a = max(min(cos_a, 1.0), -1.0)

        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        length = self.get_length()

        if length == 0:
            return 0

        cos_a = self.y_coord / length
        cos_a = max(min(cos_a, 1.0), -1.0)

        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)

        new_x = self.x_coord * math.cos(
            radians
        ) - self.y_coord * math.sin(radians)
        new_y = self.x_coord * math.sin(
            radians
        ) + self.y_coord * math.cos(radians)

        return Vector(new_x, new_y)
