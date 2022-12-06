from __future__ import annotations
import math


class Vector:
    def __init__(self, x_input: float, y_input: float) -> None:
        self.x = round(x_input, 2)
        self.y = round(y_input, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @staticmethod
    def create_vector_by_two_points(
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        len_vector = self.get_length()
        return Vector(self.x / len_vector, self.y / len_vector)

    def angle_between(self, other: Vector) -> int:
        vector_self = (self.x ** 2 + self.y ** 2) ** 0.5
        vector_other = (other.x ** 2 + other.y ** 2) ** 0.5
        cos_corner = (self.x * other.x + self.y * other.y) /\
                     (vector_self * vector_other)
        return round(math.degrees(math.acos(cos_corner)))

    def get_angle(self) -> int:
        other_x = 0
        other_y = 1
        vector_self = (self.x ** 2 + self.y ** 2) ** 0.5
        vector_other = (other_x ** 2 + other_y ** 2) ** 0.5
        cos_corner = (self.x * other_x + self.y * other_y) /\
                     (vector_self * vector_other)
        return round(math.degrees(math.acos(cos_corner)))

    def rotate(self, corner: float) -> Vector:
        cos = math.cos(math.radians(corner))
        sin = math.sin(math.radians(corner))
        return Vector(
            cos * self.x - sin * self.y,
            sin * self.x + cos * self.y
        )
