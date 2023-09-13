from __future__ import annotations
from __future__ import division
import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        scalar_product = (self.x * other.x) + (self.y * other.y)
        return scalar_product

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: Vector,
            end_point: Vector
    ) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, vector: any) -> int:
        dot_product = self.x * vector.x + self.y * vector.y
        length_product = self.get_length() * vector.get_length()
        cos_angle = dot_product / length_product
        angle_radians = math.acos(cos_angle)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def get_angle(self) -> int:
        res = math.atan2(self.x, self.y)
        if round(math.degrees(res)) < 0:
            return -round(math.degrees(res))
        return round(math.degrees(res))

    def rotate(self, num: int) -> any:
        rad = num * math.pi / 180
        sin = math.sin(rad)
        cos = math.cos(rad)
        new_x = self.x * cos - self.y * sin
        new_y = self.x * sin + self.y * cos
        return Vector(new_x, new_y)
