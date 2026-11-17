from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coordinate: float | int, y_coordinate: float | int) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, int | float):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        return round(math.degrees(
            math.acos((self.x * other.x + self.y * other.y)
                      / (self.get_length() * other.get_length()))))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        return Vector(round((self.x * math.cos(math.radians(degrees))
                             - self.y * math.sin(math.radians(degrees))), 2),
                round((self.x * math.sin(math.radians(degrees))
                       + self.y * math.cos(math.radians(degrees))), 2))