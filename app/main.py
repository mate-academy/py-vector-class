from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, float | int):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        y_vector = Vector(0, 1)
        return self.angle_between(y_vector)

    def rotate(self, degree: int) -> Vector:
        x_2 = (math.cos(math.radians(degree))
               * self.x - math.sin(math.radians(degree)) * self.y)
        y_2 = (math.sin(math.radians(degree))
               * self.x + math.cos(math.radians(degree)) * self.y)
        return Vector(x_2, y_2)


vector = Vector(33, 8)
vector1 = Vector(-4.44, 5.2)
vector2 = Vector(15, -76)

print(vector.rotate(1).x, vector.rotate(1).y)
