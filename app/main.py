from __future__ import annotations


import math


class Vector:

    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(round(self.x - other.x, 2), round(self.y - other.y, 2))

    def __mul__(self, other: float | Vector) -> Vector | float:
        if type(other) is float or type(other) is int:
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        else:
            return self.x * other.x + self.y * other.y

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
        length = (self.x ** 2 + self.y ** 2) ** 0.5
        return length

    def get_normalized(self) -> Vector:
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other: Vector) -> float:
        dot_prod = self.__mul__(other)
        x, y = self.get_length(), other.get_length()
        cos_a = dot_prod / (x * y)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        positive_y_axis = Vector(0, 1)
        return self.angle_between(positive_y_axis)

    def rotate(self, degrees: int) -> Vector:
        cos = math.cos(math.radians(degrees))
        sin = math.sin(math.radians(degrees))
        return Vector(
            round(self.x * cos - self.y * sin, 2),
            round(self.x * sin + self.y * cos, 2)
        )
