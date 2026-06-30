from __future__ import annotations
import math


class Vector:
    def __init__(self, coord_x: int, coord_y: int) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> None:
        x_new = round(self.x + other.x , 2)
        y_new = round(self.y + other.y, 2)
        return Vector(x_new, y_new)

    def __sub__(self, other: Vector) -> None:
        x_new = round(self.x - other.x, 2)
        y_new = round(self.y - other.y, 2)
        return Vector(x_new, y_new)

    def __mul__(self, other: Vector | int | float) -> None:
        if isinstance(other, (int, float)):
            new_x = round(self.x * other, 2)
            new_y = round(self.y * other, 2)
            return Vector(new_x, new_y)
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            return dot_product
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls, start_point: Vector,
                                    end_point: Vector) -> None:

        new_vector = cls(end_point[0] - start_point[0],
                         end_point[1] - start_point[1])
        return new_vector

    def get_length(self) -> float:
        return ((self.x ** 2) + (self.y ** 2)) ** (0.5)

    def get_normalized(self) -> None:
        new_x = self.x / Vector.get_length(self)
        new_y = self.y / Vector.get_length(self)
        return Vector(new_x, new_y)

    def angle_between(self, other: Vector) -> int:
        cos_angle = (Vector.__mul__(self, other)
                     / (Vector.get_length(self)
                        * Vector.get_length(other)))
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> None:
        cos_angle = self.y / Vector.get_length(self)
        return round(math.degrees(math.acos(cos_angle)))

    def rotate(self, other: int) -> None:
        new_x = (math.cos(math.radians(other)) * self.x
                 - math.sin(math.radians(other)) * self.y)
        new_y = (math.sin(math.radians(other)) * self.x
                 + math.cos(math.radians(other)) * self.y)
        return Vector(new_x, new_y)
