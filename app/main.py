from __future__ import annotations
import math


class Vector:
    # write your code here
    def __init__(self, x_cor: float | int, y_cor: float | int) -> Vector:
        self.x = round(x_cor, 2)
        self.y = round(y_cor, 2)

    def __add__(self, other_vector: Vector) -> Vector:
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    def __sub__(self, other_vector: Vector) -> Vector:
        return Vector(self.x - other_vector.x, self.y - other_vector.y)

    def __mul__(self, multiplier: Vector | float | int) -> Vector | float:
        if isinstance(multiplier, float | int):
            return Vector(self.x * multiplier, self.y * multiplier)
        return self.x * multiplier.x + self.y * multiplier.y

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other_vector: Vector) -> int:
        dot = self * other_vector
        cos_angle = dot / (self.get_length() * other_vector.get_length())
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        sine = math.sin(math.radians(degrees))
        cosine = math.cos(math.radians(degrees))
        x_rot = cosine * self.x - sine * self.y
        y_rot = sine * self.x + cosine * self.y
        return Vector(x_rot, y_rot)
