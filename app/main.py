from __future__ import annotations
import math


class Vector:
    def __init__(self, ox: float, oy: float) -> any:
        self.x = round(ox, 2)
        self.y = round(oy, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            ox=self.x + other.x,
            oy=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            ox=self.x - other.x,
            oy=self.y - other.y
        )

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, float | int):
            return Vector(
                ox=self.x * other,
                oy=self.y * other
            )
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            ox=end_point[0] - start_point[0],
            oy=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        koef = 1 / self.get_length()
        return Vector(
            ox=self.x * koef,
            oy=self.y * koef
        )

    def angle_between(self, other: Vector) -> int:
        length = self.x * other.x + self.y * other.y
        cosine = length / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cosine)))

    def get_angle(self) -> any:
        positive_y = Vector(0, 1)
        return self.angle_between(positive_y)

    def rotate(self, degrees: int) -> Vector:
        cos = math.cos(math.radians(degrees))
        sin = math.sin(math.radians(degrees))
        return Vector(
            ox=self.x * cos - self.y * sin,
            oy=self.x * sin + self.y * cos
        )
