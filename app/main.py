from __future__ import annotations
import math


class Vector:
    def __init__(self, coordinate_x: float,
                 coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other: Vector) -> Vector:
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            new_x = self.x * other.x
            new_y = self.y * other.y
            return new_x + new_y
        else:
            new_x = self.x * other
            new_y = self.y * other
            return Vector(new_x, new_y)

    @classmethod
    def create_vector_by_two_points(cls, stars_point: tuple,
                                    end_point: tuple) -> Vector:
        new_x = end_point[0] - stars_point[0]
        new_y = end_point[1] - stars_point[1]
        return Vector(new_x, new_y)

    def get_length(self) -> float:
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        new_x = self.x / length
        new_y = self.y / length
        return Vector(new_x, new_y)

    def angle_between(self, other_vector: Vector) -> int:
        dot_product = self * other_vector
        first_length = self.get_length()
        second_length = other_vector.get_length()
        if first_length == 0 or second_length == 0:
            raise ValueError("Vectors lengths should not be 0")
        cos_angle = dot_product / (first_length * second_length)
        cos_angle = max(min(cos_angle, 1), -1)
        angle = math.degrees(math.acos(cos_angle))
        return round(angle)

    def get_angle(self) -> int:
        angle = math.degrees(math.atan2(self.x, self.y))
        return round(abs(angle))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_radians = math.cos(radians)
        sin_radians = math.sin(radians)
        new_x = cos_radians * self.x - sin_radians * self.y
        new_y = sin_radians * self.x + cos_radians * self.y
        return Vector(new_x, new_y)
