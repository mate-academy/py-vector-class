from __future__ import annotations
import math


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: int | float | Vector) -> Vector:
        if isinstance(other, Vector):
            coordinate_x = self.x + other.x
            coordinate_y = self.y + other.y
            return Vector(coordinate_x, coordinate_y)

    def __sub__(self, other: int | float | Vector) -> Vector:
        if isinstance(other, Vector):
            coordinate_x = self.x - other.x
            coordinate_y = self.y - other.y
            return Vector(coordinate_x, coordinate_y)

    def __mul__(self, other: int | float | Vector) -> Vector:
        if isinstance(other, int | float):
            coordinate_x = self.x * other
            coordinate_y = self.y * other
            return Vector(coordinate_x, coordinate_y)
        elif isinstance(other, Vector):
            coordinate_x = self.x * other.x
            coordinate_y = self.y * other.y
            dot_product = coordinate_x + coordinate_y
            return dot_product

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        cls.start_point = start_point
        cls.end_point = end_point

        start_x, start_y = start_point
        end_x, end_y = end_point
        return cls(
            end_x - start_x,
            end_y - start_y
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length != 0:
            coordinate_x = self.x / length
            coordinate_y = self.y / length
            return Vector(coordinate_x, coordinate_y)

    def angle_between(self, other: Vector) -> int | float:
        scalar = self * other
        length_self = self.get_length()
        length_other = other.get_length()

        if length_self != 0 and length_other != 0:
            cosine = scalar / (length_self * length_other)
            degrees = math.degrees(math.acos(cosine))
            return round(degrees)

    def get_angle(self) -> float:
        angle_degrees = math.degrees(
            math.atan2(self.x, self.y))
        return abs(round(angle_degrees))

    def rotate(self, degrees: int | float) -> Vector:
        radians = math.radians(degrees)
        coordinate_x = round(
            self.x * math.cos(
                radians) - self.y * math.sin(radians), 2)
        coordinate_y = round(
            self.x * math.sin(
                radians) + self.y * math.cos(radians), 2)
        return Vector(coordinate_x, coordinate_y)
