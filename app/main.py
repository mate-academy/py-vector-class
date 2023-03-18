from __future__ import annotations
import math


class Vector:
    # write your code here
    def __init__(self, x_x: int | float, y_y: int | float) -> None:
        self.x_x = round(x_x, 2)
        self.y_y = round(y_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x_x + other.x_x, self.y_y + other.y_y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x_x - other.x_x, self.y_y - other.y_y)

    def __mul__(self, other: int | float) -> Vector | int:
        if isinstance(other, Vector):
            return self.x_x * other.x_x + self.y_y * other.y_y
        return Vector(self.x_x * other, (self.y_y * other))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x_x**2 + self.y_y**2)

    def get_normalized(self) -> Vector:
        return Vector(self.x_x / self.get_length(), self.y_y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        return round(math.degrees(math.acos((self.x_x * other.x_x + self.y_y *
                                             other.y_y) / (self.get_length() *
                                                           math.sqrt(other.x_x**2 + other.y_y**2)))))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        x_x = round(self.x_x * cos_a - self.y_y * sin_a, 2)
        y_y = round(self.x_x * sin_a + self.y_y * cos_a, 2)
        return Vector(x_x, y_y)
