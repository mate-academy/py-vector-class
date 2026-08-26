from __future__ import annotations
import math


class Vector:
    def __init__(
            self,
            dot_x: float | int,
            dot_y: float | int
    ) -> None:

        self.x = round(dot_x, 2)
        self.y = round(dot_y, 2)

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
            self,
            other: float | int | Vector
    ) -> Vector | float | int:

        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            dot_start: tuple,
            dot_end: tuple
    ) -> Vector:

        return cls(dot_end[0] - dot_start[0],
                   dot_end[1] - dot_start[1])

    def get_length(self) -> float:
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def get_normalized(self) -> Vector:
        normal = 1.0 / self.get_length()
        return Vector(self.x * normal, self.y * normal)

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (
                self.get_length() * other.get_length()
        )
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        oy = Vector(0, 1)
        cos_a = (self * oy) / (
                self.get_length() * oy.get_length()
        )
        print(cos_a)
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degree: int) -> Vector:
        cos_degree = math.cos(math.radians(degree))
        sin_degree = math.sin(math.radians(degree))
        dot_x = self.x * cos_degree - self.y * sin_degree
        dot_y = self.x * sin_degree + self.y * cos_degree
        return Vector(dot_x, dot_y)
