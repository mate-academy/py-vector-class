from __future__ import annotations
import math


class Vector:
    def __init__(self, x_cor: float, y_cor: float) -> None:
        self.x = round(x_cor, 2)
        self.y = round(y_cor, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __mul__(self, num: float | Vector) -> Vector | float:
        if isinstance(num, Vector):
            return self.x * num.x + self.y * num.y
        else:
            return Vector(self.x * num, self.y * num)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x**2 + self.y**2)**0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(),
                      self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        cos_theta = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_theta)))

    def get_angle(self) -> int:
        other = Vector(0, 1)
        cos_theta = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_theta)))

    def rotate(self, degrees: int) -> Vector:
        cos_a = math.cos(math.radians(degrees))
        sin_a = math.sin(math.radians(degrees))
        x2 = (cos_a * self.x) - (sin_a * self.y)
        y2 = sin_a * self.x + cos_a * self.y
        return Vector(x2, y2)
