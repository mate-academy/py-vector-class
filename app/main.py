from __future__ import annotations
import math


class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                self.x + other.x,
                self.y + other.y
            )

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                self.x - other.x,
                self.y - other.y
            )

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[int | float],
            end_point: tuple[int | float]) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int | float:
        scalar_product = self.x * other.x + self.y * other.y
        self_length = self.get_length()
        other_length = other.get_length()
        cos_theta = scalar_product / (self_length * other_length)
        theta_radians = math.acos(cos_theta)
        return round(math.degrees(theta_radians))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: int) -> Vector:
        angle_radian = math.radians(angle)
        cos = math.cos(angle_radian)
        sin = math.sin(angle_radian)
        new_x = self.x * cos - self.y * sin
        new_y = self.x * sin + self.y * cos
        return Vector(new_x, new_y)
