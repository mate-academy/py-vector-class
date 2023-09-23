from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:     # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        # return scaled vector
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        # return dot product
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return self * (1 / self.get_length())

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return int(round(math.degrees(math.acos(cos_a)), 0))

    def get_angle(self) -> int:
        return self.angle_between(Vector.y_axis())

    def rotate(self, degrees: int) -> Vector:
        # x2=cosβx1−sinβy1; y2=sinβx1+cosβy1
        return Vector(
            math.cos(math.radians(degrees)) * self.x
            - math.sin(math.radians(degrees)) * self.y,

            math.sin(math.radians(degrees)) * self.x
            + math.cos(math.radians(degrees)) * self.y
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start: tuple[int, float],
            end: tuple[int, float]
    ) -> Vector:
        return cls(end[0] - start[0], end[1] - start[1])

    def __str__(self) -> str:
        return f"({self.x}, {self.y}); length = {self.get_length()}"

    @classmethod
    def y_axis(cls) -> Vector:
        return cls(0, 1)
