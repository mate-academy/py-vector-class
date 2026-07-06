from __future__ import annotations
import math


class Vector:

    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, vector: Vector) -> Vector | None:
        if isinstance(vector, Vector):
            return Vector((self.x + vector.x), (self.y + vector.y))
        return None

    def __sub__(self, vector: Vector) -> Vector | None:
        if isinstance(vector, Vector):
            return Vector((self.x - vector.x), (self.y - vector.y))
        return None

    def __mul__(self, vector: Vector | float | int) -> Vector | float | int:
        if isinstance(vector, Vector):
            return (self.x * vector.x) + (self.y * vector.y)
        return Vector((self.x * vector), (self.y * vector))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self) -> float | int:
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def get_normalized(self) -> Vector:
        x = self.x / Vector.get_length(self)
        y = self.y / Vector.get_length(self)
        return Vector(x, y)

    def angle_between(self, vector: Vector) -> float | int:
        cos_a = (self * vector) / (self.get_length() * vector.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int | float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        rad = math.radians(degrees)
        new_x = self.x * math.cos(rad) - self.y * math.sin(rad)
        new_y = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector(new_x, new_y)