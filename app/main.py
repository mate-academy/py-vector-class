from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coord: int, y_coord: int) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int) -> int | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> Vector:
        return cls((end_point[0] - start_point[0]),
                   (end_point[1] - start_point[1]))

    def get_length(self) -> float | int:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, vector: Vector) -> int:
        cos = (self * vector) / (self.get_length() * vector.get_length())
        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> int:
        cos = self.y / self.get_length()
        return round(math.degrees(math.acos(cos)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(self.x * math.cos(radians) - self.y * math.sin(radians),
                      self.y * math.cos(radians) + self.x * math.sin(radians))
