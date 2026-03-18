from __future__ import annotations
import math


class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> float | Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            return dot_product

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
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = self.x * other.x + self.y * other.y
        self_length = self.get_length()
        other_length = other.get_length()
        cos_a = dot_product / (self_length * other_length)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        positive_y_axis = Vector(0, 1)
        return self.angle_between(positive_y_axis)

    def rotate(self, degrees: int) -> Vector:
        convert_degrees = math.radians(degrees)
        x_2 = math.cos(convert_degrees) * self.x - math.sin(convert_degrees) * self.y
        y_2 = math.sin(convert_degrees) * self.x + math.cos(convert_degrees) * self.y
        return Vector(x_2, y_2)
