from __future__ import annotations
import math


class Vector:
    def __init__(self, _x: int | float, _y: int | float) -> None:
        self.x = round(_x, 2)
        self.y = round(_y, 2)

    def __add__(self, other: Vector) -> Vector:
        new_vector_add = Vector(self.x + other.x, self.y + other.y)
        return new_vector_add

    def __sub__(self, other: Vector) -> Vector:
        new_vector_sub = Vector(self.x - other.x, self.y - other.y)
        return new_vector_sub

    def __mul__(self, other: int | float | Vector) -> \
            Vector | float | tuple | int:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(self.x * other, (self.y * other))

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(round(self.x / self.get_length(), 2),
                      round(self.y / self.get_length(), 2))

    def angle_between(self, other: Vector) -> float:
        angle = ((self.x * other.x + self.y * other.y)
                 / (self.get_length() * other.get_length()))
        return round(math.degrees(math.acos(angle)))

    def get_angle(self) -> float:
        angle = (self.x * 0 + self.y * ((self.y ** 2) ** 0.5)) / \
                (self.get_length() * Vector(0, self.y).get_length())
        return round(math.degrees(math.acos(angle)))

    def rotate(self, angle: int) -> Vector:
        return Vector(
            math.cos(math.radians(angle)) * self.x
            - math.sin(math.radians(angle)) * self.y,
            math.sin(math.radians(angle)) * self.x
            + math.cos(math.radians(angle)) * self.y)
