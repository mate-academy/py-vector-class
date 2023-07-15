from __future__ import annotations
from math import sqrt, acos, degrees, radians, cos, sin


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        mult = self.__mul__(other)
        l1 = self.get_length()
        l2 = other.get_length()
        cos_of_angle = mult / (l1 * l2)
        return round(degrees(acos(cos_of_angle)))

    def get_angle(self) -> float:
        other = Vector(0, 1)
        return self.angle_between(other)

    def rotate(self, rotate_degree: float) -> Vector:
        x_out = (self.x * cos(radians(rotate_degree))
                 - self.y * sin(radians(rotate_degree)))
        y_out = (self.x * sin(radians(rotate_degree))
                 + self.y * cos(radians(rotate_degree)))
        return Vector(x_out, y_out)
