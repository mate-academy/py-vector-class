from __future__ import annotations
import math


class Vector:

    def __init__(self, x_value: int | float, y_value: int | float) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: Vector) -> Vector:
        self.x = round(self.x + other.x, 2)
        self.y = round(self.y + other.y, 2)
        return self

    def __sub__(self, other: Vector) -> Vector:
        self.x = round(self.x - other.x, 2)
        self.y = round(self.y - other.y, 2)
        return self

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            return dot_product
        elif isinstance(other, int | float):
            self.x = round(self.x * other, 2)
            self.y = round(self.y * other, 2)
            return self

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            round(end_point[0] - start_point[0], 2),
            round(end_point[1] - start_point[1], 2)
        )

    def get_length(self) -> int | float:
        vector_length = math.sqrt(abs(self.x ** 2) + abs(self.y ** 2))
        return vector_length

    def get_normalized(self) -> Vector:
        length = Vector.get_length(self)
        self.x = round(self.x / length, 2)
        self.y = round(self.y / length, 2)
        return self

    def angle_between(self, other: Vector) -> int:
        cos_a = math.degrees(
            math.acos(self.__mul__(other)
                      / (Vector.get_length(self) * Vector.get_length(other))))
        return int(round(cos_a, 0))

    def get_angle(self) -> int:
        cos_b = math.degrees(math.acos(self.y / Vector.get_length(self)))
        return int(round(cos_b, 0))

    def rotate(self, degrees: int) -> Vector:
        cos = math.cos(math.radians(degrees))
        sin = math.sin(math.radians(degrees))
        saved_x = self.x
        self.x = round(self.x * cos - self.y * sin, 2)
        self.y = round(self.y * cos + saved_x * sin, 2)
        return self
