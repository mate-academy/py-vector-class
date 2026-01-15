from __future__ import annotations
import math


class Vector:
    def __init__(self,
                 x_coodinate: int | float,
                 y_coodinate: int | float) -> None:
        self.x = round(x_coodinate, 2)
        self.y = round(y_coodinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> float | Vector:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2)**(1 / 2)

    def get_normalized(self) -> Vector:
        vector_len = Vector.get_length(self)
        return Vector(self.x / vector_len, self.y / vector_len)

    def angle_between(self, other: Vector) -> int:
        angle_cos = (self * other) / (self.get_length() * other.get_length())
        angle_rad = math.acos(angle_cos)
        return round(math.degrees(angle_rad))

    def get_angle(self) -> int:
        vector_y = Vector.create_vector_by_two_points((0, 0,), (0, 1,))
        return self.angle_between(vector_y)

    def rotate(self, degrees: int) -> Vector:
        x2 = math.cos(math.radians(degrees)) * self.x \
            - math.sin(math.radians(degrees)) * self.y
        y2 = math.sin(math.radians(degrees)) * self.x \
            + math.cos(math.radians(degrees)) * self.y
        return Vector(x2, y2)
