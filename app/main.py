from __future__ import annotations
import math


class Vector:

    def __init__(self, first: float, second: float) -> None:
        self.x = round(first, 2)
        self.y = round(second, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        cos = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: int) -> Vector:
        r_angle = math.radians(angle)
        return Vector(math.cos(r_angle) * self.x - math.sin(r_angle) * self.y,
                      math.sin(r_angle) * self.x + math.cos(r_angle) * self.y)
