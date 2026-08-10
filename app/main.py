from __future__ import annotations
import math


class Vector:
    def __init__(self, *args) -> None:
        if len(args) == 2:
            self.x = round(args[0], 2)
            self.y = round(args[1], 2)
        else:
            self.x = 0.0
            self.y = 0.0

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(round(self.x + other.x, 2), round(self.y + other.y, 2))

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(round(self.x - other.x, 2), round(self.y - other.y, 2))

    def __mul__(self, other: Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:

        x_diff = round(end_point[0] - start_point[0], 2)
        y_diff = round(end_point[1] - start_point[1], 2)
        return cls(x_diff, y_diff)

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        exact_length = math.hypot(self.x, self.y)
        if exact_length == 0:
            raise ValueError("Неможливо нормалізувати нульовий вектор.")
        return Vector(
            round(self.x / exact_length, 2), round(self.y / exact_length, 2)
        )

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        len_self = math.hypot(self.x, self.y)
        len_other = math.hypot(other.x, other.y)

        cos_a = dot_product / (len_self * len_other)
        cos_a = max(-1.0, min(1.0, cos_a))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        positive_y_axis = Vector(0, 1)
        return self.angle_between(positive_y_axis)

    def rotate(self, degrees: int) -> "Vector":
        rad = math.radians(degrees)
        cos_a = math.cos(rad)
        sin_a = math.sin(rad)

        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a
        return Vector(round(new_x, 2), round(new_y, 2))
