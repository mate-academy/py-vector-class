from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x + other.x,
            y_coord=self.y + other.y,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x - other.x,
            y_coord=self.y - other.y
        )

    def __mul__(self, other: int | float | Vector) -> int | float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            x_coord=self.x * other,
            y_coord=self.y * other,
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[int | float],
            end_point: tuple[int | float]
    ) -> Vector:
        return cls(
            x_coord=end_point[0] - start_point[0],
            y_coord=end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()
        return Vector(
            x_coord=self.x / vector_length,
            y_coord=self.y / vector_length
        )

    def angle_between(self, another_vector: Vector) -> int:
        dot_product_of_vectors = self * another_vector
        length_of_vectors = self.get_length() * another_vector.get_length()
        cos_a = dot_product_of_vectors / length_of_vectors
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            x_coord=(self.x * math.cos(math.radians(degrees))
                     - self.y * math.sin(math.radians(degrees))),
            y_coord=(self.x * math.sin(math.radians(degrees))
                     + self.y * math.cos(math.radians(degrees)))
        )
