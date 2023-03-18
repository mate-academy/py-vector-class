from __future__ import annotations
import math


class Vector:
    # write your code here
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float) -> Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, (self.y * other))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        return round(math.degrees(math.acos((self.x * other.x + self.y * other.y) / (self.get_length()
                                                                               * math.sqrt(other.x**2 + other.y**2)))))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        x = round(self.x * cos_a - self.y * sin_a, 2)
        y = round(self.x * sin_a + self.y * cos_a, 2)
        return Vector(x, y)

