from __future__ import annotations
import math


class Vector:

    def __init__(self, x_ord: float, y_ord: float) -> None:
        self.x = round(x_ord, 2)
        self.y = round(y_ord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        start = cls(start_point[0], start_point[1])
        end = cls(end_point[0], end_point[1])
        return cls.__sub__(end, start)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(round(self.x / self.get_length(), 2),
                      round(self.y / self.get_length(), 2))

    def angle_between(self, other: Vector) -> int:
        skalar_mult = self.x * other.x + self.y * other.y
        modul_self = (self.x ** 2 + self.y ** 2) ** 0.5
        modul_other = (other.x ** 2 + other.y ** 2) ** 0.5
        cos_a = skalar_mult / (modul_self * modul_other)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        other = Vector(0, self.y)
        if self.y < 0:
            return 180 - self.angle_between(other)
        return self.angle_between(other)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a
        return Vector(new_x, new_y)
