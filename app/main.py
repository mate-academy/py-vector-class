from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, type(self)):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, type(self)):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: any) -> Vector:
        if isinstance(other, (int, float)):
            return Vector(round((self.x * other), 2),
                          round((self.y * other), 2))
        if isinstance(other, type(self)):
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        cls.x = round((end_point[0] - start_point[0]), 2)
        cls.y = round((end_point[1] - start_point[1]), 2)
        return Vector(cls.x, cls.y)

    def get_length(self) -> float:
        result_length = math.pow(self.x, 2) + math.pow(self.y, 2)
        return math.sqrt(result_length)

    def get_normalized(self) -> Vector:
        norm = self.get_length()
        norm_x = round(self.x / norm, 2)
        norm_y = round(self.y / norm, 2)
        return Vector(norm_x, norm_y)

    def angle_between(self, other: Vector) -> int:
        cos_degree = (self.__mul__(other)
                      / (self.get_length() * other.get_length()))
        return round(math.degrees(math.acos(cos_degree)))

    def get_angle(self) -> int:
        degree = self.y / self.get_length()
        angle_y = math.degrees(math.acos(degree))
        return round(angle_y)

    def rotate(self, degrees: int) -> Vector:
        radian_degree = math.radians(degrees)
        rotate_x = (math.cos(radian_degree) * self.x
                    - math.sin(radian_degree) * self.y)
        rotate_y = (math.sin(radian_degree) * self.x
                    + math.cos(radian_degree) * self.y)
        return Vector(rotate_x, rotate_y)
