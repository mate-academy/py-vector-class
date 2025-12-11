from __future__ import annotations
import math


class Vector:
    def __init__(self, x_point: int, y_point: int) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple)\
            -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        temp = self * other
        first_vector = pow(self.x, 2) + pow(self.y, 2)
        second_vector = pow(other.x, 2) + pow(other.y, 2)
        result = math.sqrt(first_vector * second_vector)
        return round(math.degrees(math.acos(temp / result)))

    def get_angle(self) -> float:
        temp = (self.x * 0) + (self.y * 1)
        length_first_vector = self.get_length()
        return round(math.degrees(math.acos(temp / length_first_vector * 1)))

    def rotate(self, degrees: int) -> Vector:
        temp = math.radians(degrees)
        x_vector = self.x * math.cos(temp) - self.y * math.sin(temp)
        y_vector = self.x * math.sin(temp) + self.y * math.cos(temp)
        return Vector(x_vector, y_vector)
