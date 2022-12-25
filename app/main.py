from __future__ import annotations
import math


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, float | int):
            return Vector(self.x * other,
                          self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @staticmethod
    def create_vector_by_two_points(start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        inv_length = 1 / self.get_length()
        return Vector(self.x * inv_length,
                      self.y * inv_length)

    def angle_between(self, other: Vector) -> float:
        cos_a = self.__mul__(other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        cos_a = (self.x * 0 + self.y
                 * ((self.y ** 2) ** 0.5)) / (self.get_length()
                                              * Vector(0, self.y).get_length())
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, other: int) -> Vector:
        # x2=cosβx1−sinβy1
        # y2=sinβx1+cosβy1
        return Vector(math.cos(math.radians(other)) * self.x
                      - math.sin(math.radians(other)) * self.y,
                      math.sin(math.radians(other)) * self.x
                      + math.cos(math.radians(other)) * self.y)
