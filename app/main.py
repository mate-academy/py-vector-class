from __future__ import annotations
import math


class Vector:
    # write your code here
    def __init__(self, x_vector: float, y_vector: float) -> None:
        self.x = round(x_vector, 2)
        self.y = round(y_vector, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            x_add = round(self.x + other.x, 2)
            y_add = round(self.y + other.y, 2)
            return Vector(x_add, y_add)
        raise TypeError("Error")

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            x_sub = round(self.x - other.x, 2)
            y_sub = round(self.y - other.y, 2)
            return Vector(x_sub, y_sub)
        raise TypeError("Error")

    def __mul__(self, other: Vector) -> Vector | float:
        if isinstance(other, (float, int)):
            x_mul = round(self.x * other, 2)
            y_mul = round(self.y * other, 2)
            return Vector(x_mul, y_mul)
        if isinstance(other, Vector):
            dot_product = (self.x * other.x) + (self.y * other.y)
            return dot_product
        raise TypeError(
            "Vector can be multiplied only by int, float or Vector"
        )

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> Vector:
        x_vec = end_point[0] - start_point[0]
        y_vec = end_point[1] - start_point[1]
        return cls(x_vec, y_vec)

    def get_length(self) -> float:
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        else:
            x_norm = self.x / length
            y_norm = self.y / length
            return Vector(x_norm, y_norm)

    def angle_between(self, other: Vector) -> int:
        dot = self * other
        len_self = self.get_length()
        len_other = other.get_length()
        if len_self == 0 or len_other == 0:
            raise ValueError("Cannot calculate angle with zero-length vector")
        cos_a = max(min(dot / (len_self * len_other), 1), -1)
        cos_a = math.degrees(math.acos(cos_a))
        return round(cos_a)

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot calculate angle with zero-length vector")
        cos_angle = self.y / length
        cos_angle = max(min(cos_angle, 1), -1)  # захист від похибок
        angle = math.degrees(math.acos(cos_angle))
        return round(angle)

    def rotate(self, degrees: int) -> Vector:
        rad = math.radians(degrees)
        x_new = self.x * math.cos(rad) - self.y * math.sin(rad)
        y_new = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector(round(x_new, 2), round(y_new, 2))
