from __future__ import annotations

import math


class Vector:

    def rotate(self, degrees: float) -> Vector:
        length = self.get_length()
        old_angle = self.get_angle_precise()
        if self.x < 0:
            old_angle = -old_angle

        new_angle = old_angle - degrees
        new_sin = math.sin(math.radians(new_angle))
        new_cos = math.cos(math.radians(new_angle))
        new_vector = Vector(new_sin * length, new_cos * length)
        return new_vector

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def get_angle_precise(self) -> float:
        return self.angle_between_precise(Vector(0, 1))

    def angle_between(self, other: Vector) -> int:
        upper_part = self * other
        down_part = self.get_length() * other.get_length()
        angle_cos = upper_part / down_part
        result = math.degrees(math.acos(angle_cos))
        return round(result)

    def angle_between_precise(self, other: Vector) -> int:
        upper_part = self * other
        down_part = self.get_length() * other.get_length()
        angle_cos = upper_part / down_part
        result = math.degrees(math.acos(angle_cos))
        return result

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        return Vector(round(self.x / self.get_length(), 2),
                      round(self.y / self.get_length(), 2))

    def __init__(self, x_coord: int, y_coord: int) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, multiplier: float | int | Vector) -> Vector:
        if isinstance(multiplier, int) or isinstance(multiplier, float):
            return Vector(round(self.x * multiplier, 2),
                          round(self.y * multiplier, 2))
        way_one = self.x * multiplier.x + self.y * multiplier.y
        return way_one

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        result = Vector(round(end_point[0] - start_point[0], 2),
                        round(end_point[1] - start_point[1], 2))
        return result
