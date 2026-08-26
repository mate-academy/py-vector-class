from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: int | float | Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("some informative message")

    def __sub__(self, other: int | float | Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        raise TypeError("some informative message")

    def __mul__(self, other: int | float | Vector) -> int | Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        raise TypeError("some informative message")

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        x_start, y_start = start_point
        x_end, y_end = end_point
        return Vector(x_end - x_start, y_end - y_start)

    def get_length(self) -> float:
        square_sum = self.x ** 2 + self.y ** 2
        return math.sqrt(square_sum)

    def get_normalized(self) -> Vector:
        length = round(self.get_length(), 1)
        if length == 0:
            raise ValueError("Length = 0 - it`s impossible.")
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: Vector) -> int:
        dot_product = self.x * other.x + self.y * other.y

        length_self = self.get_length()
        length_other = other.get_length()

        cos_angle = dot_product / (length_self * length_other)

        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        angle_radians = math.atan2(self.x, self.y)
        return abs(round(math.degrees(angle_radians)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)

        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(new_x, new_y)
