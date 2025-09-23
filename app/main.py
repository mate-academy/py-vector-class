from __future__ import annotations
import math

class Vector:
    def __init__(self, x, y) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other: int | float | Vector) -> Vector:
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            return dot_product
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> Vector:
        if len(start_point) == 2 or len(end_point) == 2:
            return Vector(end_point[0] - start_point[0] , end_point[1] - start_point[1])
        return NotImplemented

    def get_length(self) -> float:
        if self.x == 0 and self.y == 0:
            return 0
        return math.sqrt(self.x * self.x + self.y * self.y)

    def get_normalized(self) -> Vector:
        if self.x == 0 and self.y == 0:
            return Vector(0, 0)
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        if self.x == 0 and self.y == 0 or other.x == 0 and other.y == 0:
            return 0
        if isinstance(other, Vector):
            data = (self * other) / (self.get_length() * other.get_length())
            angle = math.degrees(math.acos(max(-1 ,min(1, data))))
            return round(angle)
        return NotImplemented