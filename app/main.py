from __future__ import annotations
import math


class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, number: int | Vector) -> Vector | float:
        if isinstance(number, Vector):
            return self.x * number.x + self.y * number.y
        return Vector(self.x * number, self.y * number)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple[int, int],
                                    end_point: tuple[int, int]
                                    ) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        dot_product = self.x * other.x + self.y * other.y
        length_product = self.get_length() * other.get_length()
        cos_a = dot_product / length_product
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        other_vector = Vector(0, 1)
        return self.angle_between(other_vector)

    def rotate(self, number: int) -> Vector:
        return Vector(math.cos(math.radians(number)) * self.x
                      - math.sin(math.radians(number)) * self.y,
                      math.sin(math.radians(number)) * self.x
                      + math.cos(math.radians(number)) * self.y)
