from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: int | float) -> Vector:
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: int | float) -> Vector:
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: int | float) -> Vector:
        if not isinstance(other, Vector):
            return Vector((self.x * other), (self.y * other))
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(), self.y / self.get_length()
        )

    def angle_between(self, other: int | float) -> int | float:
        return round(
            math.degrees(math.acos(
                self * other / (self.get_length() * other.get_length())))
        )

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, rotate: int) -> Vector:
        x_new = ((math.cos(math.radians(rotate)) * self.x)
                 - (math.sin(math.radians(rotate)) * self.y))
        y_new = ((math.sin(math.radians(rotate)) * self.x)
                 + (math.cos(math.radians(rotate)) * self.y))
        return Vector(x_new, y_new)
