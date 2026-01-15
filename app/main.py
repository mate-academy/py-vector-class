from __future__ import annotations


import math


class Vector:
    def __init__(self, x_value: float, y_value: float) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            round(self.x + other.x, 2),
            round(self.y + other.y, 2)
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            round(self.x - other.x, 2),
            round(self.y - other.y, 2)
        )

    def __mul__(self, other: Vector | float) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(
                round(self.x * other, 2),
                round(self.y * other, 2)
            )

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            round(end_point[0] - start_point[0], 2),
            round(end_point[1] - start_point[1], 2)
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other: Vector) -> int:
        if self.get_length() == 0 or other.get_length() == 0:
            raise ValueError("Cannot compute angle with zero vector")
        dot_product = self * other
        cos_a = dot_product / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        angle = math.atan2(self.x, self.y)
        angle_degrees = round(math.degrees(angle))
        return abs(angle_degrees)

    def rotate(self, degrees: int) -> Vector:
        radian = math.radians(degrees)
        x2 = round(math.cos(radian) * self.x - math.sin(radian) * self.y, 2)
        y2 = round(math.sin(radian) * self.x + math.cos(radian) * self.y, 2)
        return Vector(x2, y2)
