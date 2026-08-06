from __future__ import annotations
import math


class Vector:
    def __init__(self, x_axis: int | float, y_axis: int | float) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(
            (end_point[0] - start_point[0]), (end_point[1] - start_point[1])
        )

    def get_length(self) -> int | float:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector((self.x / length), (self.y / length))

    def angle_between(self, vector: Vector) -> int | float:
        product = self.__mul__(vector)
        length_product = self.get_length() * vector.get_length()
        angle = math.degrees(math.acos(product / length_product))
        return round(angle)

    def get_angle(self) -> int | float:
        return round(self.angle_between(Vector(0, 1)))

    def rotate(self, degrees: int) -> Vector:
        angle_cos = math.cos(math.radians(degrees))
        angle_sin = math.sin(math.radians(degrees))
        return Vector(
            (angle_cos * self.x - angle_sin * self.y),
            (angle_sin * self.x + angle_cos * self.y),
        )
