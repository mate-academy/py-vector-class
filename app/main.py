from __future__ import annotations
import math


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, int | float):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> int | float:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, vector: Vector) -> int:
        return round(
            math.degrees(
                math.acos((self * vector)
                          / (self.get_length() * vector.get_length()))
            )
        )

    def get_angle(self) -> int:
        vec = Vector(0, 1)
        return self.angle_between(vec)

    def rotate(self, degrees: int) -> Vector:
        angle = math.radians(degrees)
        cos_theta = math.cos(angle)
        sin_theta = math.sin(angle)
        new_x = round(self.x * cos_theta - self.y * sin_theta, 2)
        new_y = round(self.x * sin_theta + self.y * cos_theta, 2)
        return Vector(new_x, new_y)
