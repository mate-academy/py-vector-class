from __future__ import annotations
import math


class Vector:
    def __init__(self, vectors_x: float, vectors_y: float) -> None:
        self.vectors_x = vectors_x
        self.vectors_y = vectors_y

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.vectors_x + other.vectors_x,
                      self.vectors_y + other.vectors_y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.vectors_x - other.vectors_x,
                      self.vectors_y - other.vectors_y)

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            first = self.vectors_x * other.vectors_x
            second = self.vectors_y * other.vectors_y
            return first + second
        first = self.vectors_x * other
        second = self.vectors_y * other
        return first + second

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            vectors_x=end_point[0] - start_point[0],
            vectors_y=end_point[1] - start_point[1]

        )

    def get_length(self) -> float:
        return math.sqrt((self.vectors_x ** 2) + (self.vectors_y ** 2))

    def get_normalized(self) -> Vector:
        self.vectors_x /= self.get_length()
        self.vectors_y /= self.get_length()
        return self

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
        self.vectors_x = self.vectors_x * math.cos(radians)
        - self.vectors_y * math.sin(radians)
        self.vectors_y = self.vectors_x * math.sin(radians)
        + self.vectors_y * math.cos(radians)
        return self
