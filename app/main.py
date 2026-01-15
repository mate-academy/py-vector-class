from __future__ import annotations
import math


class Vector:
    def __init__(self, vector_x: int | float, vector_y: int | float) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | float | int:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        vector_x = end_point[0] - start_point[0]
        vector_y = end_point[1] - start_point[1]
        return cls(vector_x, vector_y)

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        x_normalized = self.x / length
        y_normalized = self.y / length
        return Vector(x_normalized, y_normalized)

    def angle_between(self, other: Vector) -> int:
        dot_product = (self.x * other.x) + (self.y * other.y)
        magnitude_product = self.get_length() * other.get_length()
        if magnitude_product == 0:
            return 0  # Handle the case of zero magnitude
        cos_theta = dot_product / magnitude_product
        angle_in_radians = math.acos(cos_theta)
        return round(math.degrees(angle_in_radians))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_vector_x = (self.x * math.cos(radians)
                        - self.y * math.sin(radians))
        new_vector_y = (self.x * math.sin(radians)
                        + self.y * math.cos(radians))
        return Vector(new_vector_x, new_vector_y)
