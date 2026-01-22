from __future__ import annotations
import math


class Vector:
    def __init__(self, x_point: int | float, y_point: int | float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(other * self.x, other * self.y)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        x_point = end_point[0] - start_point[0]
        y_point = end_point[1] - start_point[1]
        return cls(x_point, y_point)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        lenght = self.get_length()
        return Vector(self.x / lenght, self.y / lenght)

    def angle_between(self, other: Vector) -> float:
        dot_product = self * other
        lengths = self.get_length() * other.get_length()
        cos_angle = dot_product / lengths
        angle_radians = math.acos(cos_angle)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def get_angle(self) -> float:
        positive_y_axis = Vector(0, 1)
        return self.angle_between(positive_y_axis)

    def rotate(self, degrees: int | float) -> Vector:
        radians = math.radians(degrees)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)

        new_x = self.x * cos_angle - self.y * sin_angle
        new_y = self.x * sin_angle + self.y * cos_angle

        return Vector(new_x, new_y)
