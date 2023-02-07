from __future__ import annotations
import math


class Vector:

    def __init__(
            self, first_coord: int | float, second_coord: int | float
    ) -> None:
        self.x = round(first_coord, 2)
        self.y = round(second_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> int | float | Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, first_point: tuple,
                                    second_point: tuple) -> Vector:
        return cls(second_point[0] - first_point[0],
                   second_point[1] - first_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other_vector: Vector) -> int:
        return round(math.degrees(math.acos((self.x * other_vector.x
                                             + self.y * other_vector.y)
                                            / (self.get_length()
                                            * other_vector.get_length()))))

    def get_angle(self) -> int:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: int) -> Vector:
        return Vector(self.x * math.cos(math.radians(degrees))
                      - self.y * math.sin(math.radians(degrees)),
                      self.y * math.cos(math.radians(degrees))
                      + self.x * math.sin(math.radians(degrees)))
