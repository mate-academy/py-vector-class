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

    def __mul__(self, other: int | float | Vector) -> Vector | float | int:
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            return dot_product

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
        return Vector(
            x_coord=end_point[0] - start_point[0],
            y_coord=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            x_coord=self.x / self.get_length(),
            y_coord=self.y / self.get_length()
        )

    def angle_between(self, other_vector: Vector) -> int:
        return round(
            math.degrees(
                math.acos(
                    self.__mul__(other_vector)
                    / (self.get_length()
                       * other_vector.get_length())
                )
            )
        )

    def get_angle(self) -> int:
        return self.angle_between(Vector(x_coord=0, y_coord=1))

    def rotate(self, degrees: int) -> Vector:
        cos_degree = math.cos(math.radians(degrees))
        sin_degree = math.sin(math.radians(degrees))
        return Vector(
            x_coord=cos_degree * self.x - sin_degree * self.y,
            y_coord=sin_degree * self.x + cos_degree * self.y
        )
