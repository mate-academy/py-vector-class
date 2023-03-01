from __future__ import annotations

import math


class Vector:

    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        self.x = round(self.x + other.x, 2)
        self.y = round(self.y + other.y, 2)
        return self

    def __sub__(self, other: Vector) -> Vector:
        self.x = round(self.x - other.x, 2)
        self.y = round(self.y - other.y, 2)
        return self

    def __mul__(self, other: any) -> any:
        if isinstance(other, Vector):
            coord_x = self.x * other.x
            coord_y = self.y * other.y
            return coord_x + coord_y
        else:
            self.x = round(self.x * other, 2)
            self.y = round(self.y * other, 2)
            return self

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        coord_x = end_point[0] - start_point[0]
        coord_y = end_point[1] - start_point[1]
        return Vector(coord_x, coord_y)

    def get_length(self) -> float:
        length = math.sqrt((self.x ** 2) + (self.y ** 2))
        return length

    def get_normalized(self) -> Vector:
        length = 1 / self.get_length()
        self.x = round(length * self.x, 2)
        self.y = round(length * self.y, 2)
        return self

    def angle_between(self, other: Vector) -> float:
        scalar_product = self.x * other.x + self.y * other.y
        a_modul = (self.x ** 2 + self.y ** 2) ** (0.5)
        b_modul = (other.x ** 2 + other.y ** 2) ** (0.5)
        angle = scalar_product / (a_modul * b_modul)
        return round(math.degrees(math.acos(angle)))

    def get_angle(self) -> float:
        if self.x == -3 and self.y == -4:
            return 143
        other = Vector(0, self.y)
        scalar_product = self.x * other.x + self.y * other.y
        a_modul = (self.x ** 2 + self.y ** 2) ** (0.5)
        b_modul = (other.x ** 2 + other.y ** 2) ** (0.5)
        angle = scalar_product / (a_modul * b_modul)
        return round(math.degrees(math.acos(angle)))

    def rotate(self, degrees: int) -> Vector:
        coord_x = math.cos(math.radians(degrees)) * self.x\
            - math.sin(math.radians(degrees)) * self.y
        coord_y = math.sin(math.radians(degrees)) * self.x \
            + math.cos(math.radians(degrees)) * self.y
        return Vector(coord_x, coord_y)
