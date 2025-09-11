from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            return dot_product

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> Vector:
        first_x, first_y = start_point
        second_x, second_y = end_point
        x_new = second_x - first_x
        y_new = second_y - first_y
        return cls(x_new, y_new)

    def get_length(self) -> float | int:
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        return length

    def get_normalized(self) -> Vector:
        lenght = self.get_length()
        return Vector(self.x / lenght, self.y / lenght)

    def angle_between(self, other: Vector) -> float | int:
        dot = self.__mul__(other)
        len = self.get_length() * other.get_length()
        cos_theta = dot / len
        angle = math.degrees(math.acos(cos_theta))
        return round(angle)

    def get_angle(self) -> float | int:
        length = self.get_length()
        cos_theta = self.y / length
        angle = math.degrees(math.acos(cos_theta))
        return round(angle)

    def rotate(self, degrees: int) -> Vector:
        theta_rad = math.radians(degrees)
        x_new = self.x * math.cos(theta_rad) - self.y * math.sin(theta_rad)
        y_new = self.x * math.sin(theta_rad) + self.y * math.cos(theta_rad)
        return Vector(round(x_new, 2), round(y_new, 2))
