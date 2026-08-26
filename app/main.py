from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coordinat: int | float,
                 y_coordinat: int | float) -> None:
        self.x = round(x_coordinat, 2)
        self.y = round(y_coordinat, 2)

    def __add__(self, other: int | float | Vector) -> Vector:
        x_coordinat = self.x + other.x
        y_coordinat = self.y + other.y
        return Vector(x_coordinat, y_coordinat)

    def __sub__(self, other: int | float | Vector) -> Vector:
        x_coordinat = self.x - other.x
        y_coordinat = self.y - other.y
        return Vector(x_coordinat, y_coordinat)

    def __mul__(self, other: int | float | Vector) -> int | float | Vector:
        if isinstance(other, Vector):
            return (self.x
                    * other.x
                    + self.y
                    * other.y)
        if isinstance(other, (int, float)):
            x_coordinat = self.x * other
            y_coordinat = self.y * other
            return Vector(x_coordinat, y_coordinat)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        x_coordinat = end_point[0] - start_point[0]
        y_coordinat = end_point[1] - start_point[1]
        return cls(x_coordinat, y_coordinat)

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(),
                      self.y / self.get_length())

    def angle_between(self, vector: Vector) -> int:
        cos_angle = (self * vector) / (self.get_length() * vector.get_length())
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        y_coordinat = Vector(0, 1)
        cos_angle = ((self * y_coordinat)
                     / (self.get_length()
                        * y_coordinat.get_length()))
        return round(math.degrees(math.acos(cos_angle)))

    def rotate(self, degrees: int) -> Vector:
        rad = math.radians(degrees)
        x_coordinat = (math.cos(rad)
                       * self.x
                       - math.sin(rad)
                       * self.y)
        y_coordinat = (math.sin(rad)
                       * self.x
                       + math.cos(rad)
                       * self.y)
        return Vector(x_coordinat, y_coordinat)
