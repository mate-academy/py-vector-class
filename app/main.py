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

    def __mul__(self, other: float | Vector) -> Vector:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls, start_p: tuple, end_p: tuple
    ) -> Vector:
        x = end_p[0] - start_p[0]
        y = end_p[1] - start_p[1]
        return cls(round(x, 2), round(y, 2))

    def get_length(self) -> float:
        point1 = (0, 0)
        point2 = (self.x, self.y)
        length = math.dist(point1, point2)
        return length

    def get_normalized(self) -> Vector:
        inv_length = 1 / self.get_length()
        self.x = round(self.x * inv_length, 2)
        self.y = round(self.y * inv_length, 2)
        return self

    def angle_between(self, vector: Vector) -> int:
        dot_product = self.x * vector.x + self.y * vector.y
        magnitude_1 = math.sqrt(self.x ** 2 + self.y ** 2)
        magnitude_2 = math.sqrt(vector.x ** 2 + vector.y ** 2)
        angle_in_radians = math.acos(dot_product / (magnitude_1 * magnitude_2))
        angle_in_degrees = math.degrees(angle_in_radians)
        return round(angle_in_degrees)

    def get_angle(self) -> int:
        vector_y = Vector(0, 10)
        return self.angle_between(vector_y)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x = round(self.x * math.cos(radians) - self.y * math.sin(radians), 10)
        y = round(self.x * math.sin(radians) + self.y * math.cos(radians), 10)
        return Vector(x, y)
