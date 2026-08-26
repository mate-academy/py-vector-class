from __future__ import annotations
import math


class Vector:

    def __init__(self, coordinate_1: float, coordinate_2: float) -> None:
        self.x = round(coordinate_1, 2)
        self.y = round(coordinate_2, 2)

    def __str__(self) -> str:
        return str(self.x)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point : tuple,
                                    end_point : tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        cosine = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cosine)))

    def get_angle(self) -> float:
        if self.get_length() == 0:
            return 0
        cosine = self.y / self.get_length()
        cosine = max(-1, min(1, cosine))
        return round(math.degrees(math.acos(cosine)))

    def rotate(self, degrees: float) -> Vector:
        angel = math.radians(degrees)
        cos_x = math.cos(angel)
        sin_x = math.sin(angel)
        new_x = self.x * cos_x - self.y * sin_x
        new_y = self.x * sin_x + self.y * cos_x
        return Vector(new_x, new_y)
