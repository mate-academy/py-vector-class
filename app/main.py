from __future__ import annotations

import math


class Vector:
    def __init__(self, pos_x: float, pos_y: float) -> None:
        self.x = round(pos_x, 2)
        self.y = round(pos_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | int | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return cls(end[0] - start[0], end[1] - start[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        cosines = (self * other) / (self.get_length() * other.get_length())
        acosines = math.acos(cosines)
        return round(math.degrees(acosines))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: int) -> Vector:
        radians = math.radians(angle)
        x_prime = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_prime = self.x * math.sin(radians) + self.y * math.cos(radians)
        self.x = round(x_prime, 2)
        self.y = round(y_prime, 2)
        return self
