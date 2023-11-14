from __future__ import annotations
import math


class Vector:
    def __init__(self, coordinates_x: float, coordinates_y: float) -> None:
        self.x = round(coordinates_x, 2)
        self.y = round(coordinates_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: (Vector, float)) -> (Vector, float):
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @staticmethod
    def create_vector_by_two_points(
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        axis = Vector(0, abs(self.y))
        return self.angle_between(axis)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x_coord = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_coord = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(x_coord, y_coord)
