from __future__ import annotations
import math


class Vector:
    def __init__(self, x_1: (float, int), y_1: (float, int)) -> None:
        self.x = round(x_1, 2)
        self.y = round(y_1, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: (int, float, Vector)) -> (Vector, float, int):
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> (int, float):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: Vector) -> int:
        mul_vectors = self.__mul__(other)
        len_self = self.get_length()
        len_other = other.get_length()
        arg_cos = math.acos(mul_vectors / (len_self * len_other))
        return round(math.degrees(arg_cos))

    def get_angle(self) -> int:
        oy = Vector(0, self.y)
        if self.y < 0:
            return 180 - self.angle_between(oy)
        return self.angle_between(oy)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x_2 = math.cos(radians) * self.x - math.sin(radians) * self.y
        y_2 = math.sin(radians) * self.x + math.cos(radians) * self.y
        return Vector(round(x_2, 2), round(y_2, 2))
