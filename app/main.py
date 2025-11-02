from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float | int, y_coord: float | int) -> None:
        x, y = round(x_coord, 2), round(y_coord, 2)
        self.x = x
        self.y = y

    def __add__(self, other: Vector) -> Vector:
        sum_x = self.x + other.x
        sum_y = self.y + other.y
        return Vector(sum_x, sum_y)

    def __sub__(self, other: Vector) -> Vector:
        sub_x = self.x - other.x
        sub_y = self.y - other.y
        return Vector(sub_x, sub_y)

    def __mul__(self, num: int | float | Vector) -> Vector:
        if isinstance(num, Vector):
            mul_x = self.x * num.x
            mul_y = self.y * num.y
            dot_product = mul_x + mul_y
            return dot_product

        mul_x = self.x * num
        mul_y = self.y * num
        return Vector(mul_x, mul_y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: float | int,
            end_point: float | int) -> Vector:
        sub_x = end_point[0] - start_point[0]
        sub_y = end_point[1] - start_point[1]
        return cls(sub_x, sub_y)

    def get_length(self) -> float | int:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        norma = self.get_length()
        return Vector(self.x / norma, self.y / norma)

    def angle_between(self, another: Vector) -> float | int:
        dot_product = self.__mul__(another)
        length_1 = self.get_length()
        length_2 = another.get_length()
        cos_a = dot_product / (length_1 * length_2)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float | int:
        norma = self.get_length()
        cos_a = self.y / norma
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, angle: float | int) -> Vector:
        rad_a = math.radians(angle)
        x2 = math.cos(rad_a) * self.x - math.sin(rad_a) * self.y
        y2 = math.sin(rad_a) * self.x + math.cos(rad_a) * self.y
        return Vector(x2, y2)
