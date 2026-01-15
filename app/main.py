from __future__ import annotations
import math


class Vector:
    def __init__(self, x_: float, y_: float) -> None:
        self.x = round(x_, 2)
        self.y = round(y_, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            x_=end_point[0] - start_point[0],
            y_=end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            x_=self.x / self.get_length(),
            y_=self.y / self.get_length())

    def angle_between(self, vector: Vector) -> int:
        cos = (self * vector) / (self.get_length() * vector.get_length())
        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> float:
        cos = (self.y / self.get_length())
        return round(math.degrees(math.acos(cos)))

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            x_=round((self.x * (math.cos(math.radians(degrees)))
                      - self.y * (math.sin(math.radians(degrees)))), 2),
            y_=round((self.y * (math.cos(math.radians(degrees)))
                      + self.x
                      * (math.sin(math.radians(degrees)))), 2)
        )
