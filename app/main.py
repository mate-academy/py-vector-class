from __future__ import annotations
import math


class Vector:

    def __init__(self, vec_x: float, vec_y: float) -> None:
        self.x = round(vec_x, 2)
        self.y = round(vec_y, 2)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __mul__(self, other: Vector) -> Vector | float:
        if isinstance(other, float | int):
            vector = Vector

            return vector(self.x * other,
                          self.y * other)

        return (self.x * other.x) + (self.y * other.y)

    def get_length(self) -> float:
        return abs(((self.x ** 2) + (self.y ** 2)) ** 0.5)

    def get_normalized(self) -> Vector:
        inv_length = 1 / self.get_length()

        return Vector(round(self.x * inv_length, 2),
                      round(self.y * inv_length, 2))

    def angle_between(self, vector: Vector) -> float:
        cos_fi = ((self.x * vector.x) + (self.y * vector.y)) / \
                 (Vector.get_length(self) * Vector.get_length(vector))

        return round(math.degrees(math.acos(cos_fi)))

    def get_angle(self) -> float:
        cos_fi = (self.x * 0 + self.y * 1) / \
                 (Vector.get_length(self) * ((0 ** 2 + 1 ** 2) * 0.5))

        return round(math.degrees(math.acos(cos_fi)))

    def rotate(self, degrees: int) -> Vector:
        rad = math.radians(degrees)
        new_x = round(math.cos(rad) * self.x - (math.sin(rad)) * self.y, 2)
        new_y = round(math.sin(rad) * self.x + (math.cos(rad)) * self.y, 2)

        return Vector(new_x, new_y)
