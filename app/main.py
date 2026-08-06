from __future__ import annotations

import math


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(coord_x=(end_point[0] - start_point[0]),
                      coord_y=(end_point[1] - start_point[1]))

    def get_length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        cos_a = self.__mul__(other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        cos_a = (self.y / self.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, other: int) -> Vector:
        # x2=cosβx1−sinβy1
        # y2=sinβx1+cosβy1
        return Vector(math.cos(math.radians(other)) * self.x
                      - math.sin(math.radians(other)) * self.y,
                      math.sin(math.radians(other)) * self.x
                      + math.cos(math.radians(other)) * self.y)
