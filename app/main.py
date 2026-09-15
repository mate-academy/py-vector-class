from __future__ import annotations
import math


class Vector:
    def __init__(self, x_vector: float, y_vector: float) -> None:
        self.x = round(x_vector, 2)
        self.y = round(y_vector, 2)

    def __add__(self, other: Vector) -> Vector:
        vector_x = self.x + other.x
        vector_y = self.y + other.y
        return Vector(vector_x, vector_y)

    def __sub__(self, other: Vector) -> Vector:
        vector_x = self.x - other.x
        vector_y = self.y - other.y
        return Vector(vector_x, vector_y)

    def __mul__(self, other: Vector | float) -> Vector:
        if isinstance(other, Vector):
            vector_x = self.x * other.x
            vector_y = self.y * other.y
            dot_product = vector_x + vector_y
            return dot_product
        else:
            vector_x = self.x * other
            vector_y = self.y * other
            return Vector(vector_x, vector_y)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        vector_x = end_point[0] - start_point[0]
        vector_y = end_point[1] - start_point[1]
        return cls(vector_x, vector_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        vector_x = self.x / self.get_length()
        vector_y = self.y / self.get_length()
        return Vector(vector_x, vector_y)

    def angle_between(self, other: Vector) -> int:
        vector_x_y = (self.x * other.x) + (self.y * other.y)
        product_vector = self.get_length() * other.get_length()
        wynik = vector_x_y / product_vector
        kat_w_rad = math.acos(wynik)
        kat_w_stop = math.degrees(kat_w_rad)
        return round(kat_w_stop)

    def get_angle(self) -> int:
        wynik = self.y / self.get_length()
        kat_w_rad = math.acos(wynik)
        kat_w_stop = math.degrees(kat_w_rad)
        return round(kat_w_stop)

    def rotate(self, degrees: int) -> Vector:
        degrees_rad = math.radians(degrees)
        vector_x = math.cos(degrees_rad) * self.x - math.sin(
            degrees_rad) * self.y
        vector_y = math.sin(degrees_rad) * self.x + math.cos(
            degrees_rad) * self.y
        return Vector(vector_x, vector_y)
