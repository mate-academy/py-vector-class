from __future__ import annotations
import math


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @staticmethod
    def create_vector_by_two_points(
            start: tuple,
            end: tuple) -> Vector:
        return Vector(end[0] - start[0], end[1] - start[1])

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: Vector) -> int | float:
        vec = Vector(self.x * other.x, self.y * other.y)
        return round(math.degrees(math.acos((vec.x + vec.y)
                                            /
                                            (self.get_length() * other.get_length()))))

    def get_angle(self) -> int | float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int | float) -> Vector:
        deg_to_rad = math.radians(degrees)
        x_prime = self.x * math.cos(deg_to_rad) - self.y * math.sin(deg_to_rad)
        y_prime = self.x * math.sin(deg_to_rad) + self.y * math.cos(deg_to_rad)
        return Vector(round(x_prime, 2), round(y_prime, 2))
