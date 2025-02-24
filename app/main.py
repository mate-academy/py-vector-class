import math
from typing import Any
from math import sqrt, pow, cos, sin, radians


class Vector:
    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, float | int):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self) -> "Vector":
        length = Vector.get_length(self)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Any) -> float:
        multi_vectors = Vector.__mul__(self, other)
        vector_length_a = Vector.get_length(self)
        vector_length_b = Vector.get_length(other)

        cos_value = multi_vectors / (vector_length_a * vector_length_b)

        return round(math.degrees(math.acos(cos_value)))

    def get_angle(self) -> float:
        other = Vector(0, 1)
        return Vector.angle_between(self, other)

    def rotate(self, degrees: float) -> "Vector":

        rds = radians(degrees)
        point_x = self.x * cos(rds) - self.y * sin(rds)
        point_y = self.x * sin(rds) + self.y * cos(rds)

        return Vector(point_x, point_y)
