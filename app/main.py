from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coordinate: int | float,
                 y_coordinate: int | float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            round(self.x + other.x, 2),
            round(self.y + other.y, 2)
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            round(self.x - other.x, 2),
            round(self.y - other.y, 2)
        )

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, int | float):
            return Vector(
                round(self.x * other, 2),
                round(self.y * other, 2)
            )
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            round(end_point[0] - start_point[0], 2),
            round(end_point[1] - start_point[1], 2)
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            round(self.x / Vector.get_length(self), 2),
            round(self.y / Vector.get_length(self), 2)
        )

    def angle_between(self, other: Vector) -> float:
        cos_a = self.__mul__(other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        cos_a = (self.x * 0 + self.y * ((self.y ** 2) ** 0.5)) \
            / (self.get_length() * Vector(0, self.y).get_length())
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> Vector:
        x2 = math.cos(math.radians(degrees))
        y2 = math.sin(math.radians(degrees))

        return Vector(
            round(self.x * x2 - y2 * self.y, 2),
            round(self.x * y2 + x2 * self.y, 2)
        )
