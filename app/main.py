from __future__ import annotations
import math
from math import degrees


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coordinate=self.x + other.x,
            y_coordinate=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_coordinate=self.x - other.x,
            y_coordinate=self.y - other.y
        )

    def __mul__(self, other: float | int | Vector) -> Vector | float:
        if isinstance(other, (float, int)):
            return Vector(
                x_coordinate=self.x * other,
                y_coordinate=self.y * other
            )
        else:
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return Vector(
            x_coordinate=end_point[0] - start_point[0],
            y_coordinate=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()
        return Vector(
            x_coordinate=self.x / vector_length,
            y_coordinate=self.y / vector_length
        )

    def angle_between(self, other: Vector) -> int:
        dot_product = self.x * other.x + self.y * other.y
        magnitude_1 = (self.x ** 2 + self.y ** 2) ** 0.5
        magnitude_2 = (other.x ** 2 + other.y ** 2) ** 0.5
        angle_in_radians = math.acos(dot_product / (magnitude_1 * magnitude_2))
        return round(math.degrees(angle_in_radians))

    def get_angle(self) -> int:
        return abs(round(degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos = math.cos(radians)
        sin = math.sin(radians)
        return Vector(
            x_coordinate=self.x * cos - self.y * sin,
            y_coordinate=self.x * sin + self.y * cos
        )
