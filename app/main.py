from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x + other.x,
            y_coord=self.y + other.y
        )

    def __sub__(self, other: Vector | int) -> Vector:
        return Vector(
            x_coord=self.x - other.x,
            y_coord=self.y - other.y
        )

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(
                x_coord=self.x * other,
                y_coord=self.y * other
            )
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple) -> Vector:
        return cls(
            x_coord=end_point[0] - start_point[0],
            y_coord=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        if self.x == 0:
            return self.y
        if self.y == 0:
            return self.x
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(
            x_coord=self.x / length,
            y_coord=self.y / length
        )

    def angle_between(self, vector: Vector) -> int:
        cos_a = (self.__mul__(vector)
                 / (self.get_length()
                    * vector.get_length())
                 )
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            x_coord=(math.cos(math.radians(degrees)) * self.x
                     - math.sin(math.radians(degrees)) * self.y),
            y_coord=(math.cos(math.radians(degrees)) * self.y
                     + math.sin(math.radians(degrees)) * self.x)
        )
