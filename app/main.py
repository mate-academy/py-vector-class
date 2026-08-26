from __future__ import annotations
from typing import Any
import math


class Vector:
    def __init__(self, cor_x: float, cor_y: float) -> None:
        self.x = round(cor_x, 2)
        self.y = round(cor_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(cor_x=self.x + other.x, cor_y=self.y + other.y)
        else:
            raise TypeError("Trying to add an unknown term to vector")

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(cor_x=self.x - other.x, cor_y=self.y - other.y)
        else:
            raise TypeError("Trying to subtract an unknown term from vector")

    def __mul__(self, other: (Vector, float, int)) -> Any:
        if isinstance(other, (float, int)):
            return Vector(cor_x=self.x * other, cor_y=self.y * other)
        elif isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        else:
            raise TypeError("Multiplying vector by object of unknown type")

    def get_length(self) -> float:
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self) -> Vector:
        magnitude = math.sqrt(pow(self.x, 2) + pow(self.y, 2))
        if magnitude == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(cor_x=self.x / magnitude, cor_y=self.y / magnitude)

    def angle_between(self, other: Vector) -> int:
        if isinstance(other, Vector):
            first_magnitude = self.get_length()
            second_magnitude = other.get_length()
            common_magnitude = first_magnitude * second_magnitude
            dot_product = self * other
            angle_cos = dot_product / common_magnitude
            return round(math.degrees(math.acos(angle_cos)))
        else:
            raise TypeError(
                "Calculating angle between vector and object of unknown type"
            )

    def get_angle(self) -> int:
        return self.angle_between(Vector(cor_x=0, cor_y=abs(self.y)))

    def rotate(self, degrees: int) -> Vector:
        cos = math.cos(math.radians(degrees))
        sin = math.sin(math.radians(degrees))
        rotated_x = (cos * self.x) - (sin * self.y)
        rotated_y = (sin * self.x) + (cos * self.y)
        return Vector(cor_x=rotated_x, cor_y=rotated_y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_points: tuple,
            end_points: tuple
    ) -> Vector:
        return cls(
            cor_x=end_points[0] - start_points[0],
            cor_y=end_points[1] - start_points[1]
        )
