from __future__ import annotations
import math


class Vector:
    def __init__(self, x_point: int | float, y_point: int | float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x_point=self.x + other.x, y_point=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x_point=self.x - other.x, y_point=self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, int | float):
            return Vector(x_point=self.x * other, y_point=self.y * other)
        dot_product = self.x * other.x + self.y * other.y
        return dot_product

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple[int | float, int | float],
            end_point: tuple[int | float, int | float]) -> Vector:
        return cls(
            x_point=end_point[0] - start_point[0],
            y_point=end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            x_point=self.x / self.get_length(),
            y_point=self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(x_point=0, y_point=1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(new_x, new_y)
