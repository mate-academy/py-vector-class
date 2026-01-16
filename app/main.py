from __future__ import annotations
import math


class Vector:
    def __init__(self, axis_x: float, axis_y: float) -> None:
        self.x = round(axis_x, 2)
        self.y = round(axis_y, 2)

    def __add__(self, other: Vector) -> Vector:
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other: Vector) -> Vector:
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other: float | Vector) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        new_x = self.x * other
        new_y = self.y * other
        return Vector(round(new_x, 2), round(new_y, 2))

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_vector:
            tuple,
            end_vector: tuple
    ) -> Vector:
        return cls(end_vector[0] - start_vector[0],
                   end_vector[1] - start_vector[1])

    def get_length(self) -> float:
        return (abs(self.x) ** 2 + abs(self.y) ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()
        return Vector(self.x / vector_length, self.y / vector_length)

    def angle_between(self, other: Vector) -> int:
        cos_angle = (self * other) / (self.get_length() * other.get_length())
        radians = math.acos(cos_angle)
        degrees = math.degrees(radians)
        return round(degrees)

    def get_angle(self) -> int:
        axis_y = Vector(0, 1)
        cos_angle = (self * axis_y) / (self.get_length() * axis_y.get_length())
        radians = math.acos(cos_angle)
        degrees = math.degrees(radians)
        return round(degrees)

    def rotate(self, angle: int) -> Vector:
        angle = math.radians(angle)
        return Vector(
            self.x * math.cos(angle) - self.y * math.sin(angle),
            self.x * math.sin(angle) + self.y * math.cos(angle)
        )
