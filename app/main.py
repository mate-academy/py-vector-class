from __future__ import annotations
import math


class Vector:
    def __init__(self, vect_x: float, vect_y: float) -> None:
        self.x = round(vect_x, 2)
        self.y = round(vect_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: Vector | float | int) -> Vector:
        if isinstance(scalar, Vector):
            return self.dot_product(scalar)
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar: float | int) -> Vector:
        return Vector(self.x / scalar, self.y / scalar)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def dot_product(self, other: Vector) -> float:
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float]
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return self / length

    def angle_between(self, other: Vector) -> int:
        dot_prod = self.dot_product(other)
        len_self = self.get_length()
        len_other = other.get_length()
        if len_self == 0 or len_other == 0:
            return 0.0
        cos_angle = dot_prod / (len_self * len_other)
        cos_angle = max(min(cos_angle, 1), -1)  # Clamp to [-1, 1]
        return int(round(math.degrees(math.acos(cos_angle)), 0))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: int) -> Vector:
        radians = math.radians(angle)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        new_x = self.x * cos_angle - self.y * sin_angle
        new_y = self.x * sin_angle + self.y * cos_angle
        return Vector(new_x, new_y)
