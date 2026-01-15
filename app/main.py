from __future__ import annotations

import math


class Vector:
    def __init__(self, new_x: float, new_y: float) -> None:
        self.x = round(new_x, 2)
        self.y = round(new_y, 2)

    def __add__(self, other: Vector) -> Vector:
        self.x = round(self.x + other.x, 2)
        self.y = round(self.y + other.y, 2)

        return self

    def __sub__(self, other: Vector) -> Vector:
        self.x = round(self.x - other.x, 2)
        self.y = round(self.y - other.y, 2)

        return self

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, (float, int)):
            self.x = round(self.x * other, 2)
            self.y = round(self.y * other, 2)

            return self

        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    point_1: tuple,
                                    point_2: tuple) -> Vector:
        return Vector(point_2[0], point_2[1]) - Vector(point_1[0], point_1[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(round(self.x / self.get_length(), 2),
                      round(self.y / self.get_length(), 2))

    def angle_between(self, vector: Vector) -> float:
        dot = self * vector
        mult_length = self.get_length() * vector.get_length()
        angle_rad = math.acos(dot / mult_length)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def get_angle(self) -> float:
        angle_rad = math.acos(self.y / self.get_length())
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)

        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(round(new_x, 2), round(new_y, 2))
