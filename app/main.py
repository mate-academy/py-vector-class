from __future__ import annotations
import math


class Vector:
    def __init__(self, coord_x: int | float, coord_y: int | float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        sum_of_x = self.x + other.x
        sum_of_y = self.y + other.y
        return Vector(sum_of_x, sum_of_y)

    def __sub__(self, other: Vector) -> Vector:
        sub_of_x = self.x - other.x
        sub_of_y = self.y - other.y
        return Vector(sub_of_x, sub_of_y)

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, (float, int)):
            mul_of_x = self.x * other
            mul_of_y = self.y * other
            return Vector(mul_of_x, mul_of_y)
        mul_of_x = self.x * other.x
        mul_of_y = self.y * other.y
        return mul_of_x + mul_of_y

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        sub_of_x = end_point[0] - start_point[0]
        sub_of_y = end_point[1] - start_point[1]
        return Vector(sub_of_x, sub_of_y)

    def get_length(self) -> float:
        x_squared = self.x * self.x
        y_squared = self.y * self.y
        addition_x_and_y = x_squared + y_squared
        return math.sqrt(addition_x_and_y)

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()
        value_for_x = self.x / vector_length
        value_for_y = self.y / vector_length
        return Vector(value_for_x, value_for_y)

    def angle_between(self, vector: Vector) -> int:
        dot_product = self * vector
        self_length = self.get_length()
        vector_length = vector.get_length()
        cos_angle = dot_product / (self_length * vector_length)
        angle_in_radians = math.acos(cos_angle)
        angle_in_degrees = math.degrees(angle_in_radians)
        return math.ceil(angle_in_degrees)

    def get_angle(self) -> int:
        positive_y = Vector(0, 1)
        dot_product = (self.x * positive_y.x) + (self.y * positive_y.y)
        self_length = self.get_length()
        y_vector_length = positive_y.get_length()
        cos_angle = dot_product / (self_length * y_vector_length)
        angle_in_radians = math.acos(cos_angle)
        angle_in_degrees = math.degrees(angle_in_radians)
        return math.floor(angle_in_degrees)

    def rotate(self, degrees: int) -> Vector:
        deg_rad = math.radians(degrees)
        new_x = (self.x * math.cos(deg_rad)) - (self.y * math.sin(deg_rad))
        new_y = (self.x * math.sin(deg_rad)) + (self.y * math.cos(deg_rad))
        return Vector(new_x, new_y)
