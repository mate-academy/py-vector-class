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

    def __mul__(self, other: Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2),
                          round(self.y * other, 2))
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        cos_a = max(min(cos_a, 1), -1)
        angle_radians = math.acos(cos_a)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def get_angle(self) -> int:
        length = self.get_length()
        cos_a = self.y / length if length != 0 else 1
        angle_radians = math.acos(cos_a)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        new_x_coordinate = (self.x * cos_angle - self.y * sin_angle)
        new_y_coordinate = (self.x * sin_angle + self.y * cos_angle)
        return Vector(new_x_coordinate, new_y_coordinate)
