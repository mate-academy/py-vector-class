from __future__ import annotations
import math


class Vector:

    def __init__(self, x: (int, float), y: (int, float)) -> Vector:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other: Vector) -> Vector:
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __mul__(self, other: (Vector, int, float)) -> Vector:
        if isinstance(other, (int, float)):
            x = self.x * other
            y = self.y * other
            return Vector(x, y)
        return self.x * other.x + self.y * other.y

    def create_vector_by_two_points(self, other: tuple) -> Vector:
        x = other[0] - self[0]
        y = other[1] - self[1]
        return Vector(x, y)

    def get_length(self):
        return round((self.x**2 + self.y**2)**0.5, 2)

    def get_normalized(self) -> Vector:
        x = 1 / self.get_length() * self.x
        y = 1 / self.get_length() * self.y
        return Vector(x, y)

    def angle_between(self, vector1: Vector) -> int:
        dot_product = self.__mul__(vector1)
        vec2_length = vector1.get_length()
        vec1_length = self.get_length()
        cos_a = dot_product / (vec1_length * vec2_length)
        return  round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        axis_y = Vector(0, 1) 
        dot_product = self.__mul__(axis_y)
        vec2_length = axis_y.get_length()
        vec1_length = self.get_length()
        cos_a = dot_product / (vec1_length * vec2_length)
        return  round(math.degrees(math.acos(cos_a)))

    def rotate(self, grad: int) -> Vector:
        angle = grad * math.pi / 180
        x = self.x * math.cos(angle) - self.y * math.sin(angle)
        y = self.x * math.sin(angle) + self.y * math.cos(angle)
        return Vector(x, y)
