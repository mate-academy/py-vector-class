from __future__ import annotations
import math


class Vector:
    def __init__(self, x_0: float, y_0: float) -> None:
        self.x = round(x_0, 2)
        self.y = round(y_0, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector) -> Vector | float:
        if type(other) == float or type(other) == int:
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> object:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, vector: Vector) -> float:
        cos = (self * vector) / (self.get_length() * vector.get_length())
        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> float:
        y_vector = Vector(0, 1)
        return self.angle_between(y_vector)

    def rotate(self, degrees: int) -> Vector:
        new_x = round(self.x * math.cos(math.radians(degrees))
                      - self.y * math.sin(math.radians(degrees)), 2)
        new_y = round(self.x * math.sin(math.radians(degrees))
                      + self.y * math.cos(math.radians(degrees)), 2)
        self.x, self.y = new_x, new_y
        return self
