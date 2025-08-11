from __future__ import annotations
import math


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        coordinate_x = self.x + other.x
        coordinate_y = self.y + other.y
        return Vector(coordinate_x, coordinate_y)

    def __sub__(self, other: Vector) -> Vector:
        coordinate_x = self.x - other.x
        coordinate_y = self.y - other.y
        return Vector(coordinate_x, coordinate_y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

        coordinate_x = self.x * other
        coordinate_y = self.y * other
        return Vector(coordinate_x, coordinate_y)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple,
            end_point: tuple) -> Vector:
        coordinate_x = end_point[0] - start_point[0]
        coordinate_y = end_point[1] - start_point[1]
        return cls(coordinate_x, coordinate_y)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        coordinate_x = self.x / length
        coordinate_y = self.y / length
        return Vector(coordinate_x, coordinate_y)

    def angle_between(self, vector: Vector) -> float:
        cos = (self * vector) / (self.get_length() * vector.get_length())
        angle = math.degrees(math.acos(cos))
        return round(angle)

    def get_angle(self) -> float:
        cos = self.y / self.get_length()
        angle = math.degrees(math.acos(cos))
        return round(angle)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        coordinate_x = (
            (self.x * math.cos(radians))
            - (self.y * math.sin(radians))
        )
        coordinate_y = (
            (self.x * math.sin(radians))
            + (self.y * math.cos(radians))
        )
        return Vector(coordinate_x, coordinate_y)
