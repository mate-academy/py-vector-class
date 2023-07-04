from __future__ import annotations

from math import sqrt, acos, degrees, radians, sin, cos


class Vector:
    def __init__(self, x: int | float,
                 y: int | float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other) -> Vector:
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other) -> Vector:
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, int | float):
            return Vector(self.x * other,
                          self.y * other)
        return self.x * other.x + self.y * other.y

    @staticmethod
    def create_vector_by_two_points(start_point: tuple,
                                    end_point: tuple) -> Vector:
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return Vector(x, y)

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        x = self.x / length
        y = self.y / length
        return Vector(x, y)

    def angle_between(self, other: Vector) -> int:
        dot_product = self.__mul__(other)
        length_a, length_b = self.get_length(), other.get_length()
        angle_rad = acos((dot_product / (length_a * length_b)))
        return round(degrees(angle_rad))

    def get_angle(self) -> int:
        angle = acos((0 * self.x + 1 * self.y) / self.get_length())
        return round(degrees(angle))

    def rotate(self, angle_deg: int) -> Vector:
        angle_rad = radians(angle_deg)
        x = self.x * cos(angle_rad) - self.y * sin(angle_rad)
        y = self.x * sin(angle_rad) + self.y * cos(angle_rad)
        return Vector(x, y)
