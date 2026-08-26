from __future__ import annotations
import math
from typing import Union


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
            self,
            other: Union[Vector, int, float]
    ) -> Union[Vector, float]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return None

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple[float, float], end_point: tuple[float, float]
    ) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        cos_a = dot_product / (self.get_length() * other.get_length())
        cos_a = max(-1, min(1, cos_a))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> Vector:
        rad = math.radians(degrees)
        new_x = self.x * math.cos(rad) - self.y * math.sin(rad)
        new_y = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector(new_x, new_y)
