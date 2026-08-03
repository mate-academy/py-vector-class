from __future__ import annotations
import math


class Vector:
    def __init__(self, x_value: float, y_value: float) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x , self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x , self.y - other.y)

    def __mul__(self, other: Vector) -> Vector | int | float:
        if isinstance(other, (int | float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        cls.x = end_point[0] - start_point[0]
        cls.y = end_point[1] - start_point[1]
        return Vector(cls.x, cls.y)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        cos_a = self.__mul__(other) / (self.get_length() * other.get_length())
        result = math.degrees(math.acos(cos_a))
        return math.ceil(result)

    def get_angle(self) -> int:
        cos_a = self.y / self.get_length()
        result = math.degrees(math.acos(cos_a))
        return math.floor(result)

    def rotate(self, degrees: int | float) -> Vector:
        radians = math.radians(degrees)
        rotated_x = math.cos(radians) * self.x - math.sin(radians) * self.y
        rotated_y = math.sin(radians) * self.x + math.cos(radians) * self.y
        return Vector(rotated_x, rotated_y)
