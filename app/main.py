from __future__ import annotations
import math
from typing import Union


class Vector:
    def __init__(self, x_cor: float, y_cor: float) -> None:
        self.x = round(x_cor, 2)
        self.y = round(y_cor, 2)

    def get_length(self) -> float:
        # length = self.get_length()
        # if length == 0:
        #     return Vector(0, 0)
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[float, Vector]) -> float | Vector:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float, float],
            end_point: tuple[float, float]
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        lengths_mult = self.get_length() * other.get_length()
        if lengths_mult == 0:
            return 0
        cos_angle = max(-1, min(1, dot_product / lengths_mult))
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        if self.x == 0:
            return 0
        normalized = self.get_normalized()
        cos_angle = normalized.y
        return math.floor(math.degrees(math.acos(cos_angle)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = round(
            self.x * math.cos(radians) - self.y * math.sin(radians), 2
        )
        new_y = round(
            self.x * math.sin(radians) + self.y * math.cos(radians), 2
        )
        return Vector(new_x, new_y)
