from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None: # noqa
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        x_temp = self.x + other.x
        y_temp = self.y + other.y
        return Vector(x_temp, y_temp)

    def __sub__(self, other: Vector) -> Vector:
        x_temp = self.x - other.x
        y_temp = self.y - other.y
        return Vector(x_temp, y_temp)

    def __mul__(self, other: Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            x_temp = self.x * other
            y_temp = self.y * other
            return Vector(x_temp, y_temp)
        elif isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            return dot_product

    @classmethod
    def create_vector_by_two_points(cls, start_point: float,
                                    end_point: float) -> Vector:
        x = end_point[0] - start_point[0] # noqa
        y = end_point[1] - start_point[1] # noqa
        return cls(x, y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> float:
        dot_product = self.x * other.x + self.y * other.y
        cos_angle = dot_product / (self.get_length() * other.get_length())
        angle_in_degrees = math.degrees(math.acos(cos_angle))
        return round(angle_in_degrees)

    def get_angle(self) -> float:
        cos_angle = self.y / self.get_length()
        angle_in_degrees = math.degrees(math.acos(cos_angle))
        return round(angle_in_degrees)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
