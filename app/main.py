from __future__ import annotations
import math


class Vector:
    def __init__(self, x_point: float | int, y_point: float | int) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, Vector):
            return ((self.x * other.x)
                    + (self.y * other.y))
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        x_point = round(self.x / self.get_length(), 2)
        y_point = round(self.y / self.get_length(), 2)
        return Vector(x_point, y_point)

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = (self.x * math.cos(radians)
                 - self.y * math.sin(radians))
        new_y = (self.x * math.sin(radians)
                 + self.y * math.cos(radians))
        return Vector(new_x, new_y)
