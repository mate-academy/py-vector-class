from __future__ import annotations
import math


class Vector:
    def __init__(self, first_cord: float, second_cord: float) -> None:
        self.first_cord = round(first_cord, 2)
        self.second_cord = round(second_cord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.first_cord + other.first_cord,
                      self.second_cord + other.second_cord)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.first_cord - other.first_cord,
                      self.second_cord - other.second_cord)

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, float) or isinstance(other, int):
            return Vector(round(self.first_cord * other, 2),
                          round(self.second_cord * other, 2))

        return ((self.first_cord * other.first_cord)
                + (self.second_cord * other.second_cord))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        x_new = end_point[0] - start_point[0]
        y_new = end_point[1] - start_point[1]
        return cls(x_new, y_new)

    def get_length(self) -> float:
        return math.sqrt(self.first_cord ** 2 + self.second_cord ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(round(self.first_cord / length, 2),
                      round(self.second_cord / length, 2))

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        lengths_product = self.get_length() * other.get_length()
        if lengths_product == 0:
            raise ValueError("Cannot calculate angle with zero-length vector")
        cos_angle = dot_product / lengths_product
        angle = math.degrees(math.acos(cos_angle))
        return round(angle)

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        x_new = self.first_cord * cos_angle - self.second_cord * sin_angle
        y_new = self.first_cord * sin_angle + self.second_cord * cos_angle
        return Vector(round(x_new, 2), round(y_new, 2))
