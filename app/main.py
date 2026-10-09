from __future__ import annotations
import math
# flake8: noqa N803


class Vector:

    def __init__(self, x: float | int, y: float | int) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(round(self.x + other.x, 2),
                          round(self.y + other.y, 2))

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(round(self.x - other.x, 2),
                          round(self.y - other.y, 2))

    def __mul__(self, other: float | int | Vector) -> Vector | float:
        if isinstance(other, (float, int)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        new_x = round(end_point[0] - start_point[0], 2)
        new_y = round(end_point[1] - start_point[1], 2)
        return cls(new_x, new_y)

    def get_length(self) -> float | int:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        normalized_x = round(self.x / self.get_length(), 2)
        normalized_y = round(self.y / self.get_length(), 2)
        return Vector(normalized_x, normalized_y)

    def angle_between(self, other: Vector) -> int:
        cos_angle = ((self.x * other.x + self.y * other.y)
                     / (self.get_length() * other.get_length()))
        cos_angle = max(-1, min(1, cos_angle))
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> float | int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        new_x = round(self.x * math.cos(math.radians(degrees))
                      - self.y * math.sin(math.radians(degrees)), 2)
        new_y = round(self.x * math.sin(math.radians(degrees))
                      + self.y * math.cos(math.radians(degrees)), 2)
        return Vector(new_x, new_y)
