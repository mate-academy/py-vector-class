from __future__ import annotations

import math


class Vector:
    def __init__(self, x_cor: float, y_cor: float) -> None:
        self.x = round(x_cor, 2)
        self.y = round(y_cor, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> float | Vector:
        if isinstance(other, Vector):
            return round(self.x * other.x + self.y * other.y, 4)
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError("Unsupported type for multiplication")

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float, float],
            end_point: tuple[float, float]
    ) -> Vector:
        x_point = end_point[0] - start_point[0]
        y_point = end_point[1] - start_point[1]

        return cls(x_point, y_point)

    def get_length(self) -> float:
        length = (self.x ** 2 + self.y ** 2) ** 0.5
        return length

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ValueError("Division by 0 is not permissible")

        x_normalized = self.x / length
        y_normalized = self.y / length

        return Vector(x_normalized, y_normalized)

    def angle_between(self, vector: Vector) -> int:
        scalar_product = self.x * vector.x + self.y * vector.y

        len_self = self.get_length()
        len_other = vector.get_length()

        if len_self == 0 or len_other == 0:
            raise ValueError("Division by 0 is not permissible")

        cosine_a = scalar_product / (len_self * len_other)
        angle = math.degrees(math.acos(cosine_a))
        return round(angle)

    def get_angle(self) -> float:
        length = self.get_length()

        if length == 0:
            raise ValueError("Division by 0 is not permissible")

        cosine_a = self.y / length
        angle = math.degrees(math.acos(cosine_a))
        return round(angle)

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)

        x_rotated = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_rotated = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(round(x_rotated, 2), round(y_rotated, 2))
