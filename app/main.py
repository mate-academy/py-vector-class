from __future__ import annotations
import math


class Vector:
    def __init__(self, coordinate_x: int | float,
                 coordinate_y: int | float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: int | float) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: int | float) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float) -> Vector | float | int:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls((end_point[0] - start_point[0]),
                   (end_point[1] - start_point[1]))

    def get_length(self) -> float | int:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        norm_length = 1 / self.get_length()
        return Vector(self.x * norm_length, self.y * norm_length)

    def angle_between(self, other: int) -> int:
        cos_a = self.__mul__(other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = (self.x * 0 + self.y * abs(self.y)) \
            / (self.get_length() * Vector(0, abs(self.y)).get_length())
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, other: int) -> Vector:
        return Vector(
            self.x * math.cos(math.radians(other))
            - math.sin(math.radians(other)) * self.y,
            self.x * math.sin(math.radians(other)) + self.y
            * math.cos(math.radians(other))
        )
