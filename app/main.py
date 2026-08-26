from __future__ import annotations
import math


class Vector:
    def __init__(self, x_point: int | float, y_point: int | float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector | float | int) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x,
                          self.y + other.y)
        return NotImplemented

    def __sub__(self, other: Vector | float | int) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x,
                          self.y - other.y)
        return NotImplemented

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (float, int)):
            return Vector(x_point=self.x * other,
                          y_point=self.y * other)
        else:
            raise TypeError("Unsupported type")

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        x_point = end_point[0] - start_point[0]
        y_point = end_point[1] - start_point[1]
        return cls(x_point, y_point)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(round(self.x / length, 2),
                      round(self.y / length, 2))

    def angle_between(self, other: Vector) -> int:
        dot_prod = self * other
        length_self = self.get_length()
        length_other = other.get_length()
        cos_angle = dot_prod / (length_self * length_other)
        angle = math.degrees(math.acos(cos_angle))
        return round(angle)

    def get_angle(self) -> int:
        cos_angle = self.y / self.get_length()
        angle = math.degrees(math.acos(cos_angle))
        return round(angle)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        x_new = cos_theta * self.x - sin_theta * self.y
        y_new = sin_theta * self.x + cos_theta * self.y
        return Vector(round(x_new, 2), round(y_new, 2))
