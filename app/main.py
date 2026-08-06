from __future__ import annotations
import math


class Vector:
    # write your code here
    def __init__(self, x_point: float, y_point: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: [int, float, Vector]) -> Vector:
        return Vector(x_point=self.x + other.x, y_point=self.y + other.y)

    def __sub__(self, other: [int, float, Vector]) -> Vector:
        return Vector(x_point=self.x - other.x, y_point=self.y - other.y)

    def __mul__(self, other: [int, float, Vector]) -> [Vector, float]:
        # a · b = ax × bx + ay × by
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(x_point=self.x * other, y_point=self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        cls.x = end_point[0] - start_point[0]
        cls.y = end_point[1] - start_point[1]
        return Vector(cls.x, cls.y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        new_vector = self.get_length()
        return Vector(self.x / new_vector, self.y / new_vector)

    def angle_between(self, other: [int, float]) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = (self.x * 0 + self.y
                 * ((self.y ** 2) ** 0.5)) / (self.get_length()
                                              * Vector(0, self.y).get_length())
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, other: int) -> Vector:
        return Vector(
            x_point=math.cos(math.radians(other))
            * self.x - math.sin(math.radians(other)) * self.y,
            y_point=math.sin(math.radians(other))
            * self.x + math.cos(math.radians(other)) * self.y)
