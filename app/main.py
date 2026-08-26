from __future__ import annotations
import math


class Vector:
    def __init__(self, x1: float, y1: float) -> None:
        self.x = round(x1, 2)
        self.y = round(y1, 2)

    def __add__(self, other: Vector) -> Vector:
        x1 = self.x + other.x
        y1 = self.y + other.y
        return Vector(x1, y1)

    def __sub__(self, other: Vector) -> Vector:
        x1 = self.x - other.x
        y1 = self.y - other.y
        return Vector(x1, y1)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, int | float):
            x1 = self.x * other
            y1 = self.y * other
            return Vector(x1, y1)
        else:
            x1 = self.x * other.x
            y1 = self.y * other.y
            return x1 + y1

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        x1 = end_point[0] - start_point[0]
        y1 = end_point[1] - start_point[1]
        return Vector(x1, y1)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        x1 = self.x / self.get_length()
        y1 = self.y / self.get_length()
        return Vector(x1, y1)

    def angle_between(self, other: Vector) -> int:
        a_b = (self.x * other.x + self.y * other.y)
        a_length = self.get_length()
        b_length = other.get_length()
        len_mult = a_length * b_length
        return round(math.degrees(math.acos(a_b / len_mult)), )

    def get_angle(self) -> int:
        length = self.get_length()
        return round(math.degrees(math.acos(self.y / length)), )

    def rotate(self, deg: int) -> Vector:
        rad = math.radians(deg)
        x1 = (math.cos(rad) * self.x
              - math.sin(rad) * self.y)
        y1 = (math.sin(rad) * self.x
              + math.cos(rad) * self.y)
        return Vector(x1, y1)
