from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

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
        if isinstance(other, int | float):
            return Vector(
                self.x * other,
                self.y * other
            )
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @staticmethod
    def create_vector_by_two_points(
            start_point: tuple, end_point: tuple
    ) -> Vector:
        start_point = Vector(*start_point)
        end_point = Vector(*end_point)
        return Vector(
            end_point.x - start_point.x,
            end_point.y - start_point.y
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        vector_len = self.get_length()
        return Vector(
            self.x / vector_len,
            self.y / vector_len
        )

    def angle_between(self, other: Vector) -> float:
        if isinstance(other, Vector):
            self_len = self.get_length()
            other_len = other.get_length()
            res = self.__mul__(other) / (self_len * other_len)
        return math.ceil(math.degrees(math.acos(res)))

    def get_angle(self) -> int:
        return int(math.degrees(math.acos(self.get_normalized().y)))

    def rotate(self, other: int) -> Vector:
        radians_other = math.radians(other)
        return Vector(
            self.x * math.cos(radians_other)
            - self.y * math.sin(radians_other),
            self.x * math.sin(radians_other)
            + self.y * math.cos(radians_other)
        )
