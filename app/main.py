from __future__ import annotations
from typing import Union
import math


class Vector:
    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Union[Vector, int, float]) -> Vector:
        if not isinstance(other, Vector):
            return Vector(self.x + other, self.y + other)
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Union[Vector, int, float]) -> Vector:
        if not isinstance(other, Vector):
            return Vector(self.x - other, self.y - other)
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
            self, other: Union[Vector, int, float]
    ) -> Union[Vector, int, float]:
        if not isinstance(other, Vector):
            return Vector(self.x * other, self.y * other)
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(
            point_x=end_point[0] - start_point[0],
            point_y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        return math.ceil(
            math.degrees(
                math.acos(
                    (self * other) / (self.get_length() * other.get_length())
                )
            )
        )

    def get_angle(self) -> int:
        return int(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: Union[float, int]) -> Vector:
        radians = math.radians(degrees)

        return Vector(
            point_x=math.cos(radians) * self.x - math.sin(radians) * self.y,
            point_y=math.sin(radians) * self.x + math.cos(radians) * self.y
        )
