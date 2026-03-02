from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, v2: Vector) -> Vector:
        return Vector(self.x + v2.x, self.y + v2.y)

    def __sub__(self, v2: Vector) -> Vector:
        return Vector(self.x - v2.x, self.y - v2.y)

    def __mul__(self, mul: float | Vector) -> float | Vector:
        if isinstance(mul, Vector):
            return self.x * mul.x + self.y * mul.y
        return Vector(self.x * mul, self.y * mul)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x**2 + self.y**2)**(0.5)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, v2: Vector) -> int:
        dot_product = (self.x * v2.x + self.y * v2.y)
        cos_theta = dot_product / (self.get_length() * v2.get_length())
        return round(math.degrees(math.acos(cos_theta)))

    def get_angle(self) -> int:
        length = self.get_length()
        return round(math.degrees(math.acos(self.y / length)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta
        return Vector(new_x, new_y)
