from __future__ import annotations
import math


class Vector:

    def __init__(self, cord_x: int | float, cord_y: int | float) -> None:
        self.x = round(cord_x, 2)
        self.y = round(cord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> Vector:
        cls.x = end_point[0] - start_point[0]
        cls.y = end_point[1] - start_point[1]
        return cls(cls.x, cls.y)

    def get_length(self: Vector) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self: Vector) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self: Vector, other: Vector) -> int:
        cos_a = self.__mul__(other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self: Vector) -> int:
        if self.y > 0:
            return self.angle_between(Vector(0, self.y))
        elif self.y < 0:
            return self.angle_between(Vector(0, abs(self.y)))
        return 0

    def rotate(self: Vector, degrees: int) -> Vector:
        cos_a = math.cos(math.radians(degrees))
        sin_a = math.sin(math.radians(degrees))
        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a
        return Vector(new_x, new_y)
