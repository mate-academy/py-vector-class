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

    def __mul__(self, other: int | float | Vector) -> int | float | Vector:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(
            x_coord=self.x * other,
            y_coord=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return Vector(x_coord=end_point[0] - start_point[0],
                      y_coord=end_point[1] - start_point[1])

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(x_coord=self.x / self.get_length(),
                      y_coord=self.y / self.get_length())

    def angle_between(self, other: Vector) -> int | float:
        cos_a = self.__mul__(other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int | float:
        other = Vector(x_coord=0, y_coord=5)
        return self.angle_between(other)

    def rotate(self, degree: int) -> Vector:
        radians = math.radians(degree)
        return Vector(
            x_coord=(math.cos(radians) * self.x - math.sin(radians) * self.y),
            y_coord=(math.sin(radians) * self.x + math.cos(radians) * self.y)
        )
