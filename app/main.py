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

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(),
                      self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        cos_a = dot_product / (self.get_length()
                               * other.get_length())
        return int(
            round(
                math.degrees(
                    math.acos(max(-1, min(1, cos_a)))
                )))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_vector_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_vector_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(new_vector_x, 2), round(new_vector_y, 2))
