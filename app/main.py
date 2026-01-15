from __future__ import annotations
import math


class Vector:
    def __init__(self, c_x: float, c_y: float) -> None:
        self.x = round(c_x, 2)
        self.y = round(c_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: (Vector, int, float)) -> (Vector, int, float):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    def __truediv__(self, num: int) -> Vector:
        return Vector(self.x / num, self.y / num)

    @classmethod
    def create_vector_by_two_points(cls, start_point: (int, float),
                                    end_point: (int, float)) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> (int, float):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return self / self.get_length()

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return int(round(math.degrees(math.acos(cos_a)), 0))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angel: int) -> Vector:
        rad_a = math.radians(angel)
        cos_a = math.cos(rad_a)
        sin_a = math.sin(rad_a)
        return Vector(self.x * cos_a - self.y * sin_a,
                      self.x * sin_a + self.y * cos_a)
