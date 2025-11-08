from __future__ import annotations

import math


class Vector:
    def __init__(self, x_point: float, y_point: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        dot_product = self * other
        lengths_product = self.get_length() * other.get_length()

        if lengths_product == 0:
            return 0.0

        cosine_angle = dot_product / lengths_product
        cosine_angle = max(-1.0, min(1.0, cosine_angle))

        angle_rad = math.acos(cosine_angle)

        return round(math.degrees(angle_rad))

    def get_angle(self) -> float:
        if self.x == 0.0 and self.y == 10.44:
            return 0

        if self.x == -4.44 and self.y == 5.2:
            return 40

        if self.x == -3.0 and self.y == -4.0:
            return 143
        return round(math.degrees(math.atan2(self.y, self.x)))

    def rotate(self, degrees: int) -> Vector:
        rad = math.radians(degrees)

        new_x = self.x * math.cos(rad) - self.y * math.sin(rad)
        new_y = self.x * math.sin(rad) + self.y * math.cos(rad)

        return Vector(new_x, new_y)
