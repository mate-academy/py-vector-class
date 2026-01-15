from __future__ import annotations

import math


class Vector:
    def __init__(self, x_cord: int | float, y_cord: int | float) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    def __add__(self, other: object) -> object:
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: object) -> object:
        return Vector((self.x - other.x), (self.y - other.y))

    # def __mul__(self, other: int | float | object) -> int | float:
    def __mul__(self, other: int | float | object) -> int | float | object:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> object:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> object:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: object) -> int | float:
        cos_angle = self * other / (self.get_length() * other.get_length())
        angle_rad = math.acos(cos_angle)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def get_angle(self) -> int | float:
        y2 = abs(self.y)
        vector2 = Vector(0, y2)
        return self.angle_between(vector2)

    def rotate(self, degrees: int) -> object:
        radians = math.radians(degrees)
        cos = math.cos(radians)
        sin = math.sin(radians)

        x_cord = self.x * cos - self.y * sin
        y_cord = self.x * sin + self.y * cos

        return Vector(x_cord, y_cord)
