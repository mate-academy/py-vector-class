from __future__ import annotations
import math


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[int | float],
                                    end_point: tuple[int | float]) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        scalar_product = self * other
        cos_a = scalar_product / (self.get_length() * other.get_length())
        acos = math.acos(cos_a)
        return round(math.degrees(acos))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        rotated_x = math.cos(radians) * self.x - math.sin(radians) * self.y
        rotated_y = math.sin(radians) * self.x + math.cos(radians) * self.y
        return Vector(rotated_x, rotated_y)
