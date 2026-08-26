from __future__ import annotations
import math


class Vector:
    def __init__(self, x_axis: float, y_axis: float) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> float | Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(round(end_point[0] - start_point[0], 2),
                   round(end_point[1] - start_point[1], 2))

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()
        if vector_length > 0:
            return Vector(self.x / vector_length, self.y / vector_length)
        if vector_length == 0:
            raise ValueError("Cannot normalize the zero-length vector")
        return Vector(self.x / vector_length, self.y / vector_length)

    def angle_between(self, other: Vector) -> float:
        scalar = self.x * other.x + self.y * other.y
        v1_l = self.get_length()
        v2_l = other.get_length()
        if v1_l != 0 and v2_l != 0:
            cos_a = scalar / (v1_l * v2_l)
            return round(math.degrees(math.acos(cos_a)))
        else:
            return 0
            raise ValueError("Cannot calculate the angle "
                             "between zero-lenght vector")

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: float) -> Vector:
        x2 = (math.cos(math.radians(degrees)) * self.x
              - math.sin(math.radians(degrees)) * self.y)
        y2 = (math.sin(math.radians(degrees)) * self.x
              + math.cos(math.radians(degrees)) * self.y)
        return Vector(x2, y2)
