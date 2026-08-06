from __future__ import annotations

import math


class Vector:

    def __init__(self, x: float, y: float) -> None:     # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Vector(new_x, new_y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            new_x = self.x - other.x
            new_y = self.y - other.y
            return Vector(new_x, new_y)

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            new_x = self.x * other
            new_y = self.y * other
            return Vector(new_x, new_y)

        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        raise Exception

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]

        return Vector(new_x, new_y)

    def get_length(self) -> float:
        vector_list = [self.x, self.y]
        result_list = [i**2 for i in vector_list]

        return math.sqrt(sum(result_list))

    def get_normalized(self) -> Vector:
        new_x = self.x / self.get_length()
        new_y = self.y / self.get_length()

        return Vector(new_x, new_y)

    def angle_between(self, other: Vector) -> int:
        scalar_mul = self * other
        modul_self = math.sqrt(sum([self.x**2, self.y**2]))
        modul_other = math.sqrt(sum([other.x**2, other.y**2]))
        cos_angle = scalar_mul / (modul_self * modul_other)
        angle_deegres = math.degrees(math.acos(cos_angle))

        return round(angle_deegres)

    def get_angle(self) -> int:
        angle_radians = math.atan2(self.x, self.y)
        angle_deegres = math.degrees(angle_radians) * -1

        return round(angle_deegres)

    def rotate(self, degrees: int) -> Vector:
        angle_radians = math.radians(degrees)

        cos_x1 = math.cos(angle_radians) * self.x
        sin_y1 = math.sin(angle_radians) * self.y
        sin_x1 = math.sin(angle_radians) * self.x
        cos_y1 = math.cos(angle_radians) * self.y
        new_x = cos_x1 - sin_y1  # x2 = cosβx1−sinβy1
        new_y = sin_x1 + cos_y1   # y2 = sinβx1 + cosβy1

        return Vector(new_x, new_y)
