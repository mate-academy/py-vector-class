from __future__ import annotations
import math


class Vector:
    def __init__(self, point_x: float , point_y: float = 0) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __mul__(self, other: Vector | int) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = round(Vector.get_length(self), 2)
        x_n = round(self.x / length, 2)
        y_n = round(self.y / length, 2)
        return Vector(x_n, y_n)

    def angle_between(self, vector: Vector) -> int:
        len1 = Vector.get_length(self)
        len2 = Vector.get_length(vector)
        vec = self * vector
        cos_a = vec / (len1 * len2)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        len1 = Vector.get_length(self)
        len2 = self.y
        cos_a = len2 / len1
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        sin_a = math.sin(radians)
        cos_a = math.cos(radians)
        x2 = self.x * cos_a - self.y * sin_a
        y2 = self.x * sin_a + self.y * cos_a
        return Vector(x2, y2)
