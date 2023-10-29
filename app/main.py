from __future__ import annotations

from math import sqrt, acos, degrees, atan2, cos, sin, radians


class Vector:
    def __init__(self, cord_x: int | float, cord_y: int | float) -> None:
        self.x = round(cord_x, 2)
        self.y = round(cord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        vector_x = self.x + other.x
        vector_y = self.y + other.y
        return Vector(vector_x, vector_y)

    def __sub__(self, other: Vector) -> Vector:
        vector_x = self.x - other.x
        vector_y = self.y - other.y
        return Vector(vector_x, vector_y)

    def __mul__(self, other: int | float | Vector) -> Vector | int:
        if isinstance(other, (int, float)):
            vector_x = self.x * other
            vector_y = self.y * other
            return Vector(vector_x, vector_y)
        if isinstance(other, Vector):
            vectors_mul = self.x * other.x + self.y * other.y
            return vectors_mul

    @staticmethod
    def create_vector_by_two_points(vector_1: tuple,
                                    vector_2: tuple) -> Vector:
        x1, y1 = vector_1
        x2, y2 = vector_2
        return Vector(x2 - x1, y2 - y1)

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        vector_x = self.x / length
        vector_y = self.y / length
        return Vector(vector_x, vector_y)

    def angle_between(self, other: Vector) -> int:
        mul_vectors = self * other
        length_vectors = self.get_length() * other.get_length()
        cos_between = mul_vectors / length_vectors
        theta = acos(cos_between)
        return round(degrees(theta))

    def get_angle(self) -> int:
        return abs(round(degrees(atan2(self.x, self.y))))

    def rotate(self, angle: int) -> Vector:
        angle = radians(angle)
        rotated_x = self.x * cos(angle) - self.y * sin(angle)
        rotated_y = self.x * sin(angle) + self.y * cos(angle)
        return Vector(rotated_x, rotated_y)
