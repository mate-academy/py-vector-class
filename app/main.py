from __future__ import annotations
from typing import Union
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x_coord = round(x_coord, 2)
        self.y_coord = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x_coord + other.x_coord,
            y_coord=self.y_coord + other.y_coord
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x_coord - other.x_coord,
            y_coord=self.y_coord - other.y_coord
        )

    def __mul__(self, other: Union[Vector, float]) -> Union[Vector, float]:
        if isinstance(other, (float, int)):
            return Vector(
                x_coord=self.x_coord * other,
                y_coord=self.y_coord * other
            )
        return self.x_coord * other.x_coord + self.y_coord * other.y_coord

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            x_coord=end_point[0] - start_point[0],
            y_coord=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x_coord ** 2 + self.y_coord ** 2)

    def get_normalized(self) -> Vector:
        len_of_not_norm_vector = Vector.get_length(self)
        return Vector(
            x_coord=self.x_coord / len_of_not_norm_vector,
            y_coord=self.y_coord / len_of_not_norm_vector
        )

    def angle_between(self, second_vector: Vector) -> int:
        return round(
            math.degrees(
                math.acos(
                    self * second_vector
                    / (self.get_length() * second_vector.get_length())
                )
            )
        )

    def get_angle(self) -> int:
        second_vector = Vector(x_coord=0, y_coord=1)
        return self.angle_between(second_vector)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(
            x_coord=math.cos(radians) * self.x_coord - math.sin(radians) * self.y_coord,
            y_coord=math.sin(radians) * self.x_coord + math.cos(radians) * self.y_coord
        )
