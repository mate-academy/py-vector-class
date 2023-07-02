from typing import Union
from math import pow, sqrt, acos, degrees, sin, cos, radians

types_of_other = Union["Vector", int, float]


class Vector:
    def __init__(self, dot_x: float, dot_y: float) -> None:
        self.x = round(dot_x, 2)
        self.y = round(dot_y, 2)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":
        return cls(
            dot_x=end_point[0] - start_point[0],
            dot_y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self) -> "Vector":
        length_of_vector = self.get_length()

        return Vector(
            dot_x=round(self.x / length_of_vector, 2),
            dot_y=round(self.y / length_of_vector, 2)
        )

    def angle_between(self, other: "Vector") -> int:
        dot_product = self.x * other.x + self.y * other.y
        magnitude_of_first = sqrt(pow(self.x, 2) + pow(self.y, 2))
        magnitude_of_second = sqrt(pow(other.x, 2) + pow(other.y, 2))
        mul_of_magnitudes = magnitude_of_first * magnitude_of_second
        formula_of_angle = dot_product / mul_of_magnitudes
        degrees_of_vectors = round(degrees(acos(formula_of_angle)))

        return degrees_of_vectors

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, abs(self.y)))

    def rotate(self, deg: int) -> "Vector":
        rotated_x = cos(radians(deg)) * self.x - sin(radians(deg)) * self.y
        rotated_y = sin(radians(deg)) * self.x + cos(radians(deg)) * self.y

        return Vector(
            dot_x=round(rotated_x, 2),
            dot_y=round(rotated_y, 2)
        )

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            dot_x=self.x + other.x,
            dot_y=self.y + other.y
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            dot_x=self.x - other.x,
            dot_y=self.y - other.y
        )

    def __mul__(self, other: types_of_other) -> types_of_other:
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y

            return dot_product

        return Vector(
            dot_x=self.x * other,
            dot_y=self.y * other
        )
