from __future__ import annotations
import math


class Vector:

    def __init__(self, xx: float, yy: float) -> None:
        self.x = round(xx, 2)
        self.y = round(yy, 2)

    def __add__(self, other: Vector) -> Vector:
        xx = self.x + other.x
        yy = self.y + other.y
        return Vector(xx, yy)

    def __sub__(self, other: Vector) -> Vector:
        xx = self.x - other.x
        yy = self.y - other.y
        return Vector(xx, yy)

    def __mul__(self, other: int | float | Vector) -> Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        xx = self.x * other
        yy = self.y * other
        return Vector(xx, yy)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        xx = end_point[0] - start_point[0]
        yy = end_point[1] - start_point[1]
        return cls(xx, yy)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        xx = self.x / length
        yy = self.y / length
        return Vector(xx, yy)

    def angle_between(self, other: Vector) -> int:
        cos_a = (self.__mul__(other)
                 / (self.get_length()
                 * (other.x ** 2 + other.y ** 2) ** 0.5))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = self.y / (self.get_length() * (1 ** 2) ** 0.5)
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, angle: int) -> Vector:
        xx = (math.cos(math.radians(angle)) * self.x
              - math.sin(math.radians(angle)) * self.y)
        yy = (math.sin(math.radians(angle)) * self.x
              + math.cos(math.radians(angle)) * self.y)
        return Vector(xx, yy)
