from __future__ import annotations
import math


class Vector:
    def __init__(self, some_x: float, some_y: float) -> None:
        self.x = round(some_x, 2)
        self.y = round(some_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> float | Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        raise TypeError("Operand must be an instance of Vector, int or float")

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> float:
        length_s = self.get_length()
        length_o = other.get_length()
        cos_a = (self * other) / (length_s * length_o)
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self) -> float:
        positive_y_axis = Vector(0, 1)
        cos_a = ((self * positive_y_axis)
                 / (self.get_length() * positive_y_axis.get_length()))
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
