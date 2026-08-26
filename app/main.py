from __future__ import annotations

import math


class Vector:
    def __init__(self, first_coordinate: float,
                 second_coordinate: float) -> None:
        self.x = round(first_coordinate, 2)
        self.y = round(second_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, value: int | float | Vector) -> Vector | int | float:
        if isinstance(value, (int, float)):
            return Vector(self.x * value, self.y * value)
        elif isinstance(value, Vector):
            return self.x * value.x + self.y * value.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()
        return Vector(self.x / vector_length, self.y / vector_length)

    def angle_between(self, other: Vector) -> int:
        dot = self * other
        lengths = self.get_length() * other.get_length()

        vector_cos = dot / lengths

        angle_degrees = math.degrees(math.acos(vector_cos))

        return round(angle_degrees)

    def get_angle(self) -> int:
        cos_theta = self.y / self.get_length()

        angle_radians = math.acos(cos_theta)
        angle_degrees = math.degrees(angle_radians)

        return round(angle_degrees)

    def rotate(self, degrees: int) -> Vector:

        radians = math.radians(degrees)

        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(round(new_x, 2), round(new_y, 2))
