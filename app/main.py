from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        sum_x = round(self.x + other.x, 2)
        sum_y = round(self.y + other.y, 2)

        return Vector(sum_x, sum_y)

    def __sub__(self, other: Vector) -> Vector:
        sub_x = round(self.x - other.x, 2)
        sub_y = round(self.y - other.y, 2)

        return Vector(sub_x, sub_y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if not isinstance(other, Vector):
            mul_x = round(self.x * other, 2)
            mul_y = round(self.y * other, 2)

            return Vector(mul_x, mul_y)

        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, st_p: tuple, end_p: tuple) -> Vector:
        return Vector(end_p[0] - st_p[0], end_p[1] - st_p[1])

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()

        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        angle = self.__mul__(other) / (self.get_length() * other.get_length())

        return round(math.degrees(math.acos(angle)))

    def get_angle(self) -> int:
        other = Vector(0, 1)

        return self.angle_between(other)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x2 = math.cos(radians) * self.x - math.sin(radians) * self.y
        y2 = math.sin(radians) * self.x + math.cos(radians) * self.y

        return Vector(x2, y2)
