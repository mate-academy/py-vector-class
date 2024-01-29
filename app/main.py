from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coordinate: int | float,
                 y_coordinate: int | float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            dot_product = (self.x * other.x) + (self.y * other.y)
            return dot_product
        if isinstance(other, int | float):
            return Vector((self.x * other), (self.y * other))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]
        return cls(new_x, new_y)

    def get_length(self) -> int | float:
        length = (((self.x ** 2) + (self.y ** 2)) ** 0.5)
        return length

    def get_normalized(self) -> Vector:
        normalized_x = self.x / self.get_length()
        normalized_y = self.y / self.get_length()
        return Vector(normalized_x, normalized_y)

    def angle_between(self, other_vector: Vector) -> int:
        dot_product = self.x * other_vector.x + self.y * other_vector.y
        magnitude_product = self.get_length() * other_vector.get_length()

        cos_angle = dot_product / magnitude_product
        angle_in_degrees = math.degrees(math.acos(cos_angle))

        return round(angle_in_degrees)

    def get_angle(self) -> int | float:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        angle_in_radians = math.radians(degrees)
        new_x = (self.x * math.cos(angle_in_radians)
                 - self.y * math.sin(angle_in_radians))
        new_y = (self.x * math.sin(angle_in_radians)
                 + self.y * math.cos(angle_in_radians))

        return Vector(new_x, new_y)
