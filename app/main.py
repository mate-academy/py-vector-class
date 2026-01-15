from __future__ import annotations

import math


class Vector:
    def __init__(self, first_point: float, second_point: float) -> None:
        self.x = round(first_point, 2)
        self.y = round(second_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> float | Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float, float],
            end_point: tuple[float, float]
    ) -> Vector:
        first_point = end_point[0] - start_point[0]
        second_point = end_point[1] - start_point[1]
        return cls(first_point, second_point)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: Vector) -> int:
        dot_product = self * vector
        len1 = self.get_length()
        len2 = vector.get_length()
        if len1 == 0 or len2 == 0:
            return 0
        cos_a = dot_product / (len1 * len2)
        cos_a = max(min(cos_a, 1), -1)
        angle_rad = math.acos(cos_a)
        angle_deg = round(math.degrees(angle_rad))
        return angle_deg

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a
        return Vector(new_x, new_y)
