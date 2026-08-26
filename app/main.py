from __future__ import annotations
from math import radians, degrees, acos, sin, cos


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        mag = self.get_length()
        return Vector(self.x / mag, self.y / mag)

    def angle_between(self, vector: Vector) -> int:
        cos_a = (self.__mul__(vector)
                 / (self.get_length() * vector.get_length()))
        return round(degrees(acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: int) -> Vector:
        deg2rad = radians(angle)
        return Vector(round(cos(deg2rad) * self.x - sin(deg2rad) * self.y, 2),
                      round(sin(deg2rad) * self.x + cos(deg2rad) * self.y, 2))
