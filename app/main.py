from __future__ import annotations
import math


class Vector:
    def __init__(self, vector_x: (int, float), vector_y: (int, float)) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

    def __add__(self, other: Vector) -> Vector:
        vector_x = self.x + other.x
        vector_y = self.y + other.y
        return Vector(vector_x, vector_y)

    def __sub__(self, other: Vector) -> Vector:
        vector_x = self.x - other.x
        vector_y = self.y - other.y
        return Vector(vector_x, vector_y)

    def __mul__(self, other: (int, float, Vector)) -> (int, float, Vector):
        if isinstance(other, Vector):
            part_x = self.x * other.x
            part_y = self.y * other.y
            return part_x + part_y

        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        vector_x = end_point[0] - start_point[0]
        vector_y = end_point[1] - start_point[1]
        return cls(vector_x, vector_y)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        vector_x = self.x / self.get_length()
        vector_y = self.y / self.get_length()
        return Vector(vector_x, vector_y)

    def angle_between(self, other: Vector) -> int:
        cosine = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cosine)))

    def get_angle(self) -> int:
        vector_y = Vector(0, 1)
        return self.angle_between(vector_y)

    def rotate(self, angle: int) -> Vector:
        radians = math.radians(angle)
        cos = math.cos(radians)
        sin = math.sin(radians)
        vector_x = self.x * cos - self.y * sin
        vector_y = self.x * sin + self.y * cos
        return Vector(vector_x, vector_y)
