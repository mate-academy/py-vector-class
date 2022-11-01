from typing import Union
from math import sqrt
import math


class Vector:
    def __init__(self, x_value: Union[int, float],
                 y_value: Union[int, float]) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: Union[int, float]) -> Union:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        if isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)

    def __sub__(self, other: Union[int, float]) -> Union:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        if isinstance(other, (int, float)):
            return Vector(self.x - other, self.y - other)

    def __mul__(self, other: Union[int, float]) -> Union:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            dot_product = ((self.x * other.x) + (self.y * other.y))
            return dot_product

    @classmethod
    def create_vector_by_two_points(cls, start_point: float,
                                    end_point: float) -> Union:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> Union:
        return sqrt(self.x * self.x + self.y * self.y)

    def get_normalized(self) -> Union:
        norm_length = 1 / self.get_length()
        return Vector(self.x * norm_length, self.y * norm_length)

    def angle_between(self, other: Union[int, float]) -> Union:
        return round(math.degrees(math.acos(Vector.__mul__(self, other)
                                            / abs(Vector.get_length(self)
                                            * Vector.get_length(other)))))

    def get_angle(self) -> Union:
        return round(math.degrees(math.atan2(abs(self.x), self.y)))

    def rotate(self, degrees: int) -> Union:
        if degrees == 45:
            cs = sn = sqrt(2) / 2
        else:
            cs = math.cos(math.radians(degrees))
            sn = math.sin(math.radians(degrees))
        return Vector(self.x * cs - self.y * sn, self.y * cs + self.x * sn)
