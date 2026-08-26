from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x + other.x,
            y_coord=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x - other.x,
            y_coord=self.y - other.y
        )

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            x_coord=self.x * other,
            y_coord=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            x_coord=end_point[0] - start_point[0],
            y_coord=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()
        return Vector(
            x_coord=self.x / vector_length,
            y_coord=self.y / vector_length
        )

    def angle_between(self, second_vector: Vector) -> int:
        dot_product = self * second_vector
        vector1_magnitude = self.get_length()
        vector2_magnitude = second_vector.get_length()
        cos_a = dot_product / (vector1_magnitude * vector2_magnitude)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        vector_magnitude = self.get_length()
        cos_a = self.y / vector_magnitude
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> Vector:
        sin_a = math.sin(math.radians(degrees))
        cos_a = math.cos(math.radians(degrees))
        return Vector(
            x_coord=cos_a * self.x - sin_a * self.y,
            y_coord=sin_a * self.x + cos_a * self.y
        )
