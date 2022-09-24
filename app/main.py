from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x=self.x - other.x, y=self.y - other.y)

    def __mul__(self, other: Vector | float) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(x=self.x * other, y=self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:

        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        inv_length = 1 / self.get_length()
        return Vector(self.x * inv_length, self.y * inv_length)

    def angle_between(self, other: Vector) -> int:
        cos_a = self.__mul__(other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 5))

    def rotate(self, degrees: int) -> Vector:
        cos_a = math.cos(math.radians(degrees))
        sin_a = math.sin(math.radians(degrees))
        return Vector(self.x * cos_a - self.y * sin_a,
                      self.x * sin_a + self.y * cos_a)
