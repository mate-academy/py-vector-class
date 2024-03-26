from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            round(self.x + other.x, 2),
            round(self.y + other.y, 2)
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            round(self.x - other.x, 2),
            round(self.y - other.y, 2)
        )

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            round(self.x * other, 2),
            round(self.y * other, 2)
        )

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(round(end_point[0] - start_point[0], 2),
                   round(end_point[1] - start_point[1], 2))

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def get_normalized(self) -> Vector:
        return Vector(
            round((self.x * (1 / self.get_length())), 2),
            round((self.y * (1 / self.get_length())), 2)
        )

    def angle_between(self, other: Vector) -> float:
        dot_product = self.__mul__(other)
        length_product = self.get_length() * other.get_length()
        if length_product == 0:
            return 0
        angle_in_radians = math.acos(dot_product / length_product)
        angle_in_degrees = math.degrees(angle_in_radians)
        return int(round(angle_in_degrees))

    def get_angle(self) -> float:
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: float) -> Vector:
        angle_radians = math.radians(degrees)
        cos_angle = math.cos(angle_radians)
        sin_angle = math.sin(angle_radians)
        new_x = self.x * cos_angle - self.y * sin_angle
        new_y = self.x * sin_angle + self.y * cos_angle
        return Vector(new_x, new_y)
