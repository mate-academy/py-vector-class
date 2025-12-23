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

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, int | float):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return NotImplemented

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        mul_a_b = self * other
        mul_len_a_b = self.get_length() * other.get_length()
        return int(round(math.degrees(math.acos(mul_a_b / mul_len_a_b)), 0))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        deg_in_rad = math.radians(degrees)
        return Vector(
            math.cos(deg_in_rad) * self.x - math.sin(deg_in_rad) * self.y,
            math.sin(deg_in_rad) * self.x + math.cos(deg_in_rad) * self.y
        )
