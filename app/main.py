from __future__ import annotations
import math


class Vector:

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        len = self.get_length()
        return Vector(self.x / len , self.y / len)

    def angle_between(self, other: Vector) -> int:
        cos = self * other / (self.get_length() * other.get_length())
        angle = round(math.degrees(math.acos(cos)), 0)
        return angle

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, grad: int) -> Vector:
        # x1 = x * cos(angle) + y * sin(angle)
        # y1 = y * cos(angle) - x * sin(angle)
        rad = math.radians(grad)
        x1 = self.x * math.cos(rad) - self.y * math.sin(rad)
        y1 = self.y * math.cos(rad) + self.x * math.sin(rad)
        return Vector(x1, y1)
