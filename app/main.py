from __future__ import annotations

from typing import Union
import math


class Vector:
    def __init__(self, x_var: Union[float, int], y_var: Union[float, int])\
            -> None:
        self.x = round(x_var, 2)
        self.y = round(y_var, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[int, float, Vector])\
            -> Union[int, float, Vector]:
        if isinstance(other, Union[int, float]):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        else:
            return self.x * other.x + self.y * other.y

    @staticmethod
    def create_vector_by_two_points(start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(round(end_point[0] - start_point[0], 2),
                      round(end_point[1] - start_point[1], 2))

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        if self.get_length() != 0:
            normalized_x = self.x / self.get_length()
            normalized_y = self.y / self.get_length()
            return Vector(normalized_x, normalized_y)

    def angle_between(self, other: Vector) -> int:
        modul_a = math.sqrt(self.x ** 2 + self.y ** 2)
        modul_b = math.sqrt(other.x ** 2 + other.y ** 2)
        scal = self.x * other.x + self.y * other.y
        return round(math.degrees(math.acos(scal / (modul_a * modul_b))))

    def get_angle(self) -> int:
        angle_radians = math.atan2(self.x, self.y)
        angle_degrees = math.degrees(angle_radians)
        if angle_degrees < 0:
            return round(angle_degrees) * (-1)
        return round(angle_degrees)

    def rotate(self, degree: int) -> Vector:
        one_degree = math.radians(degree)
        b_x = self.x * math.cos(one_degree) - self.y * math.sin(one_degree)
        b_y = self.x * math.sin(one_degree) + self.y * math.cos(one_degree)
        return Vector(round(b_x, 2), round(b_y, 2))
