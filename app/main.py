from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coo: (int, float), y_coo: (int, float)) -> None:
        self.x = round(x_coo, 2)
        self.y = round(y_coo, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: (int, float, Vector)) -> (Vector, float, int):
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2),
                          round(self.y * other, 2))
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> (int, float):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(round(self.x / self.get_length(), 2),
                      round(self.y / self.get_length(), 2))

    def angle_between(self, other: Vector) -> int:
        return round(math.degrees(
            math.acos((self * other)
                      / (self.get_length()
                         * other.get_length()))))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        rad = math.radians(degrees)
        cos = math.cos(rad)
        sin = math.sin(rad)
        return Vector((cos * self.x) - (sin * self.y),
                      (sin * self.x) + (cos * self.y))
