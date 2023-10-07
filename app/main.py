from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coordinate: int, y_coordinate: int) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | int:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:

        vector1 = cls(start_point[0], start_point[1])
        vector2 = cls(end_point[0], end_point[1])
        vector_by_points = cls(vector2.x - vector1.x, vector2.y - vector1.y)

        return vector_by_points

    def get_length(self) -> float:
        vector_length = math.sqrt(self.x ** 2 + self.y ** 2)
        return vector_length

    def get_normalized(self) -> Vector:

        vector_length = self.get_length()
        normalized_x = round(self.x / vector_length, 2)
        normalized_y = round(self.y / vector_length, 2)

        return Vector(normalized_x, normalized_y)

    def angle_between(self, other: Vector | float) -> int:

        dot_product = self * other
        vector1_mag = self.get_length()
        vector2_mag = other.get_length()

        cos_a = math.acos(dot_product / (vector1_mag * vector2_mag))
        o_degree = round(math.degrees(cos_a))

        return abs(o_degree)

    def get_angle(self) -> int:

        tang_a = math.atan2(self.x, self.y)
        angle = round(math.degrees(tang_a))

        return abs(angle)

    def rotate(self, degrees: int) -> Vector:

        radians = math.radians(degrees)
        rotated_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        rotated_y = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(rotated_x, rotated_y)
