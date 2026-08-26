from __future__ import annotations
import math


class Vector:

    def __init__(self, vector_x: float | int, vector_y: float | int) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | int | Vector) -> Vector | float | int:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(round(self.x * other, 2), round(self.y * other, 2))

    def get_length(self) -> float | int:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(),
                      self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        magnitudes = self.get_length() * other.get_length()
        cosine = dot_product / magnitudes
        degrees = math.degrees(math.acos(cosine))
        return round(degrees)

    def get_angle(self) -> int:
        other = Vector(0 , 1)
        dot_product = self * other
        magnitudes = self.get_length() * other.get_length()
        cosine = dot_product / magnitudes
        degrees = math.degrees(math.acos(cosine))
        return round(degrees)

    def rotate(self, degrees: int) -> Vector:
        cos_d = math.cos(math.radians(degrees))
        sin_d = math.sin(math.radians(degrees))
        rotated_x = cos_d * self.x - sin_d * self.y
        rotated_y = sin_d * self.x + cos_d * self.y
        return Vector(rotated_x, rotated_y)
