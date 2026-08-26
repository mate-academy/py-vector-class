from __future__ import annotations
import math
from typing import Tuple, Union


class Vector:
    def __init__(self, vector_x: float, vector_y: float) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError("Can only add Vector to Vector")
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError("Can only subtract Vector from Vector")
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[float, Vector]) -> Union[Vector, float]:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        raise TypeError("Can only multiply by number or Vector")

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: Tuple[float, float],
            end_point: Tuple[float, float]
    ) -> Vector:
        vector_x = end_point[0] - start_point[0]
        vector_y = end_point[1] - start_point[1]
        return cls(vector_x, vector_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        magnitude_product = self.get_length() * other.get_length()
        if magnitude_product == 0:
            return 0
        cos_angle = dot_product / magnitude_product
        cos_angle = max(-1, min(1, cos_angle))
        angle_rad = math.acos(cos_angle)
        return round(math.degrees(angle_rad))

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        dot_product = self * y_axis
        magnitude_product = self.get_length() * y_axis.get_length()

        if magnitude_product == 0:
            return 0

        cos_angle = dot_product / magnitude_product
        cos_angle = max(-1, min(1, cos_angle))
        angle_rad = math.acos(cos_angle)
        angle_deg = math.degrees(angle_rad)

        return round(angle_deg)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos = math.cos(radians)
        sin = math.sin(radians)
        new_x = self.x * cos - self.y * sin
        new_y = self.x * sin + self.y * cos
        return Vector(round(new_x, 2), round(new_y, 2))

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"
