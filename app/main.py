from __future__ import annotations
from math import sqrt, degrees, acos, atan2, cos, sin, radians


class Vector:
    def __init__(self, x_cr: float, y_cr: float) -> None:
        self.x = round(x_cr, 2)
        self.y = round(y_cr, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple) -> Vector:
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        leng = self.get_length()
        return Vector(round(self.x / leng, 2), round(self.y / leng, 2))

    def angle_between(self, other: Vector) -> int:
        return round(
            degrees(acos((Vector.__mul__(self, other))
                         / (Vector.get_length(self)
                            * Vector.get_length(other)))))

    def get_angle(self) -> int:
        angle_rad = atan2(self.x, self.y)
        angle_deg = abs(degrees(angle_rad))
        return round(angle_deg)

    def rotate(self, degree: int) -> Vector:
        angle_rad = radians(degree)
        new_x = self.x * cos(angle_rad) - self.y * sin(angle_rad)
        new_y = self.x * sin(angle_rad) + self.y * cos(angle_rad)
        return Vector(round(new_x, 2), round(new_y, 2))
