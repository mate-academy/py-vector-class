from __future__ import annotations
from math import sqrt, degrees, acos, atan2, cos, sin, radians


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(x_coord=end_point[0] - start_point[0],
                   y_coord=end_point[1] - start_point[1])

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        cos_a = ((self.x * other.x + self.y * other.y)
                 / (sqrt(self.x ** 2 + self.y ** 2)
                 * sqrt(other.x ** 2 + other.y ** 2)))
        return round(degrees(acos(cos_a)))

    def get_angle(self) -> int:
        return abs(round(degrees(atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        new_x = (self.x * cos(radians(degrees))
                 - self.y * sin(radians(degrees)))
        new_y = (self.x * sin(radians(degrees))
                 + self.y * cos(radians(degrees)))
        return Vector(new_x, new_y)
