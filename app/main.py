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
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x**2 + self.y**2)**(1 / 2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x * 1 / self.get_length(),
            self.y * 1 / self.get_length()
        )

    def angle_between(self, other: Vector) -> float:
        cos_a = (self.x * other.x + self.y
                 * other.y) / ((self.x ** 2 + self.y ** 2) ** (1 / 2)
                               * (other.x ** 2 + other.y ** 2) ** (1 / 2))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        cos_a = self.y / ((self.x ** 2 + self.y ** 2) ** (1 / 2))
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> Vector:
        angle = math.radians(degrees)
        return Vector(
            math.cos(angle) * self.x - math.sin(angle) * self.y,
            math.sin(angle) * self.x + math.cos(angle) * self.y
        )
