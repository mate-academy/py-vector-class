from __future__ import annotations
import math

class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other: Vector) -> Vector:
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __mul__(self, other: int | float | Vector) -> Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        x = self.x * other
        y = self.y * other
        return Vector(x, y)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(x, y)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        x = self.x / length
        y = self.y / length
        return Vector(x, y)

    def angle_between(self, other: Vector) -> int:
        cos_a = (self.__mul__(other)
                 / (self.get_length()
                 * (other.x ** 2 + other.y ** 2) ** 0.5))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = self.y / (self.get_length() * (1 ** 2) ** 0.5)
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, angle: int) -> Vector:
        x = (math.cos(math.radians(angle)) * self.x
             - math.sin(math.radians(angle)) * self.y)
        y = (math.sin(math.radians(angle)) * self.x
             + math.cos(math.radians(angle)) * self.y)
        return Vector(x, y)
