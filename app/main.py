from __future__ import annotations
from math import sqrt, acos, degrees, atan2, cos, sin, radians


class Vector:
    def __init__(self, xi: float, yi: float) -> None:
        self.x = round(xi, 2)
        self.y = round(yi, 2)

    def __add__(self, other: Vector) -> Vector:
        new_v = Vector(self.x + other.x, self.y + other.y)
        return new_v

    def __sub__(self, other: Vector) -> Vector:
        new_v = Vector(self.x - other.x, self.y - other.y)
        return new_v

    def __mul__(self, other: Vector | int | float) -> Vector:
        if isinstance(other, (int, float)):
            out = Vector(self.x * other, self.y * other)
            return out
        out = self.x * other.x + self.y * other.y
        return out

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        xi = round(end_point[0] - start_point[0], 2)
        yi = round(end_point[1] - start_point[1], 2)
        return cls(xi, yi)

    def get_length(self) -> float:
        out = sqrt(self.x**2 + self.y**2)
        return out

    def get_normalized(self) -> Vector:
        norm_x = self.x / self.get_length()
        norm_y = self.y / self.get_length()
        return Vector(round(norm_x, 2), round(norm_y, 2))

    def angle_between(self, other: Vector) -> int:
        angle = degrees(acos((self * other)
                             / (self.get_length()
                             * other.get_length())))
        return int(round(angle, 0))

    def get_angle(self) -> int:
        angle = degrees(atan2(self.x, self.y))
        return abs(int(round(angle, 0)))

    def rotate(self, degree: int) -> Vector:
        rad = radians(degree)
        xi = round(self.x * cos(rad) - self.y * sin(rad), 2)
        yi = round(self.x * sin(rad) + self.y * cos(rad), 2)
        vector = Vector(xi, yi)
        return vector
