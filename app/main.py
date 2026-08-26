from __future__ import annotations

import math


class Vector:
    def __init__(self, x_cord: float, y_cord: float) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple[float, float],
                                    end_point: tuple[float, float]) -> Vector:
        x_cord = end_point[0] - start_point[0]
        y_cord = end_point[1] - start_point[1]
        return cls(x_cord, y_cord)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            lengths_product = self.get_length() * other.get_length()

            if lengths_product == 0:
                raise ValueError("Zero length vector")

            cos_theta = dot_product / lengths_product
            cos_theta = max(min(cos_theta, 1), -1)

            angle_radians = math.acos(cos_theta)
            return round(math.degrees(angle_radians))

        return NotImplemented

    def get_angle(self) -> int:
        length = self.get_length()
        cos_theta = self.y / length
        cos_theta = max(min(cos_theta, 1), -1)

        angle_radians = math.acos(cos_theta)
        return round(math.degrees(angle_radians))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)

        x_rotated = self.x * cos_theta - self.y * sin_theta
        y_rotated = self.x * sin_theta + self.y * cos_theta
        return Vector(x_rotated, y_rotated)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

        return NotImplemented

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

        return NotImplemented

    def __mul__(self, other: Vector | int | float) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

        return NotImplemented
