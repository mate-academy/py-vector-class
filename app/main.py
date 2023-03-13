from __future__ import annotations

import math


class Vector:

    def __init__(self, x: float, y: float) -> Vector:
        self.x = round(x, 2)
        self.y = round(y, 2)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return Vector(
            round(end_point[0] - start_point[0], 2),
            round(end_point[1] - start_point[1], 2)
        )

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            (self.x + other.x), (self.y + other.y)
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            (self.x - other.x), (self.y - other.y)
        )

    def __mul__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(
            round((self.x * other), 2),
            round((self.y * other), 2))

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(),
                      self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        return round(math.degrees(math.acos(
            ((self.x * (other.x) + self.y * other.y)
             / ((math.sqrt(self.x ** 2 + self.y ** 2)
                 * math.sqrt(other.x ** 2 + other.y ** 2)))))), 0)

    def get_angle(self) -> float:
        return abs(round(math.atan2(self.x, self.y) * 180 / math.pi, 0))

    def rotate(self, degrees: int) -> Vector:
        angle = math.radians(degrees)
        x_new = self.x * math.cos(angle) - self.y * math.sin(angle)
        y_new = self.x * math.sin(angle) + self.y * math.cos(angle)
        return Vector(round(x_new, 2), round(y_new, 2))
#