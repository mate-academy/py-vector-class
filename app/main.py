from typing import Union
from math import sqrt, pow
import math


class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, vector1: "Vector") -> "Vector":
        return Vector(vector1.x + self.x, vector1.y + self.y)

    def __sub__(self, vector1: "Vector") -> "Vector":
        return Vector(self.x - vector1.x, self.y - vector1.y)

    def __mul__(self, other: Union[int, float, "Vector"]) -> Union[float, "Vector"]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> "Vector":
        return cls(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self) -> float:
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> float:
        upper_mul = self * other
        length_mul = self.get_length() * other.get_length()

        if length_mul == 0:
            raise ValueError("Error")

        cos_res = upper_mul / length_mul
        res = round(math.degrees(math.acos(cos_res)))

        return res

    def get_angle(self) -> float:
        before = self.y / self.get_length()
        return round(math.degrees(math.acos(before)))

    def rotate(self, number: int) -> "Vector":
        r_num = math.radians(number)

        x_rotate = self.x * math.cos(r_num) - self.y * math.sin(r_num)
        y_rotate = self.x * math.sin(r_num) + self.y * math.cos(r_num)
        return Vector(round(x_rotate, 2), round(y_rotate, 2))
