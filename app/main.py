from __future__ import annotations
import math


class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, vector_2: Vector) -> Vector:
        return Vector(self.x + vector_2.x, self.y + vector_2.y)

    def __sub__(self, vector_2: Vector) -> Vector:
        return Vector(self.x - vector_2.x, self.y - vector_2.y)

    def __mul__(self, multiplier: Vector | int) -> float | Vector:
        if isinstance(multiplier, Vector):
            return self.x * multiplier.x + self.y * multiplier.y

        elif isinstance(multiplier, int) or isinstance(multiplier, float):
            return Vector(self.x * multiplier, self.y * multiplier)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self, vector: Vector) -> float:
        return pow((pow(vector.x, 2) + pow(vector.y, 2)), 1 / 2)

    def get_normalized(self) -> Vector:
        vector_length = self.get_length(self)
        if vector_length > 0:
            return Vector(self.x / vector_length, self.y / vector_length)

    def angle_between(self, vector_1: Vector, vector_2: Vector) -> int:
        scalar = vector_1.x * vector_2.x + vector_1.y * vector_2.y
        v1_l = self.get_length(vector_1)
        v2_l = self.get_length(vector_2)
        if v1_l != 0 and v2_l != 0:
            cos_a = scalar / (v1_l * v2_l)
            return round(math.degrees(math.acos(cos_a)))
        else:
            return 0

    def get_angle(self) -> int:
        return self.angle_between(self, Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        x2 = (math.cos(math.radians(degrees)) * self.x
              - math.sin(math.radians(degrees)) * self.y)
        y2 = (math.sin(math.radians(degrees)) * self.x
              + math.cos(math.radians(degrees)) * self.y)
        return Vector(x2, y2)
