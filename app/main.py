from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector | float) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, + self.y + other.y)
        elif isinstance(other, float):
            return Vector(self.x + other, + self.y + other)

    def __sub__(self, other: Vector | float) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        elif isinstance(other, float):
            return Vector(self.x - other, self.y - other)

    def __mul__(self, other: Vector | float) -> Vector:
        if isinstance(other, Vector):
            dot_product = (self.x * other.x) + (self.y * other.y)
            return dot_product
        return Vector(self.x * other, self.y * other)

    @staticmethod
    def vector_mul(vector: Vector, number: float) -> Vector:
        return Vector(vector.x * number, vector.y * number)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple) -> Vector:
        x1, y1 = start_point
        x2, y2 = end_point
        return cls(x2 - x1, y2 - y1)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length != 0:
            return Vector(self.x / length, self.y / length)
        else:
            return Vector(0, 0)

    def dot_product(self, other: Vector) -> float:
        return self.x * other.x + self.y * other.y

    def angle_between(self, other: Vector) -> int:
        dot_product = self.dot_product(other)
        magnitude_product = self.get_length() * other.get_length()

        if magnitude_product != 0:
            radians = math.acos(dot_product / magnitude_product)
            degrees = math.degrees(radians)
            return round(degrees)
        else:
            return 0

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x_coord = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y_coord = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(new_x_coord, new_y_coord)
