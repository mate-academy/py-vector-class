from __future__ import annotations
import math


class Vector:

    def __init__(self, x_some: int | float, y_some: int | float) -> None:
        self.x = round(x_some, 2)
        self.y = round(y_some, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        start_point = list(start_point)
        end_point = list(end_point)
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        number_x = round(self.x / self.get_length(), 2)
        number_y = round(self.y / self.get_length(), 2)
        return Vector(number_x, number_y)

    def angle_between(self, vector: Vector) -> int:
        cos_a = (self.x * vector.x + self.y * vector.y) / \
                (self.get_length() * vector.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: int) -> Vector:
        cos_a = math.cos(math.radians(degrees))
        sin_a = math.sin(math.radians(degrees))
        return Vector(cos_a * self.x - sin_a * self.y,
                      sin_a * self.x + cos_a * self.y)
