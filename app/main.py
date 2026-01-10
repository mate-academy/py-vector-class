from __future__ import annotations
import math


class Vector:
    def __init__(self, x_param: float, y_param: float) -> None:
        self.x = round(x_param, 2)
        self.y = round(y_param, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x_param=self.x + other.x, y_param=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x_param=self.x - other.x, y_param=self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if not isinstance(other, Vector):
            return Vector(x_param=self.x * other, y_param=self.y * other)
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(x_param=end_point[0] - start_point[0],
                   y_param=end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> Vector:
        return Vector(x_param=self.x / self.get_length(),
                      y_param=self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(x_param=0, y_param=1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(
            x_param=self.x * math.cos(radians) - self.y * math.sin(radians),
            y_param=self.x * math.sin(radians) + self.y * math.cos(radians),
        )
