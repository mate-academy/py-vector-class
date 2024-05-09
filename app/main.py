from __future__ import annotations
import math


class Vector:

    def __init__(self, vector_x: float, vector_y: float) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            self.x * other,
            self.y * other
        )

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, vector: Vector) -> float:
        return round(math.degrees(math.acos(
            (self * vector) / (self.get_length() * vector.get_length())
        )))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: float) -> Vector:
        degrees = math.radians(degrees)
        return Vector(
            math.cos(degrees) * self.x - math.sin(degrees)
            * self.y,
            math.sin(degrees) * self.x + math.cos(degrees)
            * self.y
        )
