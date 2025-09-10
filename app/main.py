from __future__ import annotations
import math


class Vector:

    def __init__(self, x_cord: (float, int), y_cord: (float, int)) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    def __add__(self, other: Vector | int) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: Vector | int) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other: Vector | int) -> Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple) -> Vector:
        return Vector(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float | int:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            round(
                self.x / self.get_length(), 2
            ),
            round(
                self.y / self.get_length(), 2
            )
        )

    def angle_between(self, vector: Vector) -> int:
        doc_vector = self.x * vector.x + self.y * vector.y
        length_self = self.get_length()
        vector_length = vector.get_length()
        cos_a = doc_vector / (length_self * vector_length)
        cos_a = max(min(cos_a, 1), -1)
        return int(round(math.degrees(math.acos(cos_a)), 0))

    def get_angle(self) -> angle_between:
        y_axis_vector = Vector(0, 1)
        return self.angle_between(y_axis_vector)

    def rotate(self, degress: int) -> Vector:
        radians = math.radians(degress)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
