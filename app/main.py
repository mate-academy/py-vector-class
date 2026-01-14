from __future__ import annotations
import math


class Vector:
    def __init__(self, vector_x: int | float, vector_y: int | float) -> None:
        self.vector_x = round(vector_x, 2)
        self.vector_y = round(vector_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.vector_x + other.vector_x,
                      self.vector_y + other.vector_y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.vector_x - other.vector_x,
                      self.vector_y - other.vector_y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.vector_x * other, self.vector_y * other)
        return (self.vector_x * other.vector_x
                + self.vector_y * other.vector_y)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> int:
        return (self.vector_x ** 2 + self.vector_y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.vector_x / length,
                      self.vector_y / length)

    def angle_between(self, other: Vector) -> float:
        cos = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> float:
        cos = self.vector_y / self.get_length()
        return round(math.degrees(math.acos(cos)))

    def rotate(self, degree: int) -> Vector:
        radians = math.radians(degree)

        new_x = (self.vector_x * math.cos(radians)
                 - self.vector_y * math.sin(radians))
        new_y = (self.vector_x * math.sin(radians)
                 + self.vector_y * math.cos(radians))
        return Vector(new_x, new_y)
