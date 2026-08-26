from __future__ import annotations
from math import sqrt, acos, degrees, sin, cos, radians


class Vector:
    def __init__(self, x_value: float | int, y_value: float | int) -> None:
        self.x, self.y = round(x_value, 2), round(y_value, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> int | float | Vector:
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
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: Vector) -> int:
        lengths = self.get_length() * vector.get_length()
        dot = self.x * vector.x + self.y * vector.y
        vectors_angel = round(degrees(acos(dot / lengths)))
        return vectors_angel if vectors_angel >= 0 else vectors_angel + 360

    def get_angle(self) -> float | int:
        return round(degrees(acos(self.y / self.get_length())))

    def rotate(self, degrees_rotation: int) -> Vector:
        angle_radians = radians(degrees_rotation)
        x_new = self.x * cos(angle_radians) - self.y * sin(angle_radians)
        y_new = self.x * sin(angle_radians) + self.y * cos(angle_radians)
        return Vector(x_new, y_new)
