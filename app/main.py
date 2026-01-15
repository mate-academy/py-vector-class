from __future__ import annotations

import math


class Vector:
    def __init__(self, index_x: float, index_y: float) -> None:
        self.x = round(index_x, 2)
        self.y = round(index_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x,
                          self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x,
                          self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other,
                      self.y * other)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        cosines = (self * other) / (self.get_length() * other.get_length())
        acosines = math.acos(cosines)
        return round(math.degrees(acosines))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, rotate_angle: int) -> Vector:
        radians = math.radians(rotate_angle)
        x_prime = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_prime = self.x * math.sin(radians) + self.y * math.cos(radians)
        self.x = round(x_prime, 2)
        self.y = round(y_prime, 2)
        return self

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])
