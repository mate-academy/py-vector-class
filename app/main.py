from __future__ import annotations

import math


class Vector:
    def __init__(self, coord_x: int | float, coord_y: int | float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: int | float) -> Vector:
        if isinstance(other, Vector):
            return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: int | float) -> Vector:
        if isinstance(other, Vector):
            return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: int | float) -> int | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector((self.x * other), (self.y * other))

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple,
    ) -> Vector:
        return cls(
            (end_point[0] - start_point[0]),
            (end_point[1] - start_point[1])
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector((self.x / length), (self.y / length))

    def angle_between(self, other: Vector) -> int:
        dot_product = (self.x * other.x) + (self.y * other.y)
        calc_magnitudes1 = self.get_length()
        calc_magnitudes2 = other.get_length()
        calc_cosine = dot_product / (calc_magnitudes1 * calc_magnitudes2)
        return int(round(math.degrees(math.acos(calc_cosine))))

    def get_angle(self) -> int:
        dot_product = (self.x * 0) + (self.y * 1)
        magnitude = self.get_length()
        cos_of_the_angel = dot_product / magnitude
        return int(round(math.degrees(math.acos(cos_of_the_angel))))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x_new = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_new = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(x_new, y_new)
