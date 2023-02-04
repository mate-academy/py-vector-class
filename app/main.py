from __future__ import annotations
import math


class Vector:
    def __init__(self, x_vec: float, y_vec: float) -> None:
        self.x = round(x_vec, 2)
        self.y = round(y_vec, 2)

    def __add__(self, other: Vector | int | float) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        if isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)

    def __sub__(self, other: Vector | int | float) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        if isinstance(other, (int, float)):
            return Vector(self.x - other, self.y - other)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:

        x_vec = round(end_point[0] - start_point[0], 2)
        y_vec = round(end_point[1] - start_point[1], 2)
        return Vector(x_vec, y_vec)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            round(
                self.x / self.get_length(), 2
            ), round(
                self.y / self.get_length(), 2
            ))

    def angle_between(self, other: Vector) -> int | float:
        cos = math.acos(
            self * other / (self.get_length() * other.get_length()))
        degree = round(math.degrees(cos))
        return degree

    def get_angle(self) -> int | float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, num: int) -> Vector:
        sin = math.sin(math.radians(num))
        cos = math.cos(math.radians(num))
        x_vec = (cos * self.x) - (sin * self.y)
        y_vec = sin * self.x + cos * self.y
        return Vector(x_vec, y_vec)
