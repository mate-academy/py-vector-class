from __future__ import annotations
from math import degrees, acos, sin, cos, radians


class Vector:
    def __init__(self, x: float | int, y: float | int) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        x0, y0 = start_point
        x1, y1 = end_point
        return cls(x1 - x0, y1 - y0)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other: float | int | Vector) -> float | int | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    def __sub__(self, other: Vector) -> Vector:
        return self.__add__(other * (-1))

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        modulo = self.get_length()
        return Vector(self.x / modulo, self.y / modulo)

    def angle_between(self, other: Vector) -> int:
        cosin = self.__mul__(other) / (self.get_length() * other.get_length())
        return round(degrees(acos(cosin)))

    def get_angle(self) -> int:
        positive_y = Vector(0, 1)
        return self.angle_between(positive_y)

    def rotate(self, angle: int) -> Vector:
        rad_an = radians(angle)
        rotated_x = self.x * cos(rad_an) - self.y * sin(rad_an)
        rotated_y = self.x * sin(rad_an) + self.y * cos(rad_an)
        return Vector(rotated_x, rotated_y)
