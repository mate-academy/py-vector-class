from __future__ import annotations
from typing import Tuple, Union
import math


class Vector:
    def __init__(self, x_: Union[int, float], y_: Union[int, float]) -> None:
        self.x = round(x_, 2)
        self.y = round(y_, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[Vector, int, float]) -> Union[int, Vector]:
        if type(other) is Vector:
            return self.x * other.x + self.y * other.y
        elif type(other) in (int, float):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: Tuple[Union[int, float]],
                                    end_point: Tuple[Union[int, float]]) \
            -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> int:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        self_cos = self.x / self.get_length()
        other_cos = other.x / other.get_length()

        self_degrees = math.degrees(math.acos(self_cos))
        other_degrees = math.degrees(math.acos(other_cos))
        if self.y * other.y >= 0:
            result_angle = round(abs(self_degrees - other_degrees))
        else:
            result_angle = round(self_degrees + other_degrees)
        return result_angle if result_angle <= 180 else 360 - result_angle

    def get_angle(self) -> int:
        self_cos = self.x / self.get_length()
        angle = math.degrees(math.acos(self_cos))
        if self.y >= 0:
            return round(abs(angle - 90))
        else:
            return 180 - round(abs(angle - 90))

    def rotate(self, degrees: int) -> Vector:
        self_length = self.get_length()
        self_cos = self.x / self_length
        self_degrees = math.degrees(math.acos(self_cos))
        if self.y < 0:
            self_degrees *= -1

        result_degrees = self_degrees + degrees
        result_cos = math.cos(math.radians(result_degrees))
        result_sin = math.sin(math.radians(result_degrees))
        result_x = result_cos * self_length
        result_y = result_sin * self_length
        return Vector(round(result_x, 2), round(result_y, 2))
