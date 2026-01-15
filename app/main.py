from __future__ import annotations
import math


class Vector:
    def __init__(self, start_x: int | float, end_y: int | float) -> None:
        self.x = round(start_x, 2)
        self.y = round(end_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.__dot_product(other)

        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_pont: tuple,
                                    end_point: tuple) -> Vector:
        x1, y1, x2, y2 = *start_pont, *end_point

        return cls(x2 - x1, y2 - y1)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        self_length = self.get_length()
        other_length = Vector.get_length(other)

        if self_length and other_length:
            cosine = self.__dot_product(other) / (self_length * other_length)
            cosine = max(-1, min(1, cosine))
            return int(round(math.degrees(math.acos(cosine))))

    def get_angle(self) -> int:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        angle_radians = math.radians(degrees)
        cos_theta = math.cos(angle_radians)
        sin_theta = math.sin(angle_radians)

        rotated_x = self.x * cos_theta - self.y * sin_theta
        rotated_y = self.x * sin_theta + self.y * cos_theta

        return Vector(rotated_x, rotated_y)

    def __dot_product(self, other: Vector) -> float | int:
        return self.x * other.x + self.y * other.y
