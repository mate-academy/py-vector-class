from __future__ import annotations
import math


class Vector:

    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(float(self.x) * other, float(self.y) * other)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        new_vector = cls(end[0] - start[0], end[1] - start[1])
        return new_vector

    def get_length(self) -> float:
        magnitude = math.sqrt(self.x ** 2 + self.y ** 2)
        return magnitude

    def get_normalized(self) -> Vector:
        length = self.get_length()
        norm_lenght = 1 / length
        self.x *= norm_lenght
        self.y *= norm_lenght
        return Vector(self.x, self.y)

    # @stamethod
    def angle_between(self, other: Vector) -> int:
        angle = math.acos((self.x * other.x + self.y * other.y)
                          / (self.get_length() * other.get_length()))
        return round(math.degrees(angle))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, abs(self.y)))

    def rotate(self, angle: int) -> Vector:
        cos_a = math.cos(math.radians(angle))
        sin_a = math.sin(math.radians(angle))
        x1 = cos_a * self.x - sin_a * self.y
        y1 = sin_a * self.x + cos_a * self.y
        return Vector(x1, y1)
