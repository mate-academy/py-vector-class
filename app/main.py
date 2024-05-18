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

    def __mul__(self, other: float) -> Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    def dot(self, other: Vector) -> float:
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        start_x, start_y = start_point
        end_x, end_y = end_point
        x_coordinate = end_x - start_x
        y_coordinate = end_y - start_y
        return cls(x_coordinate, y_coordinate)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** .5

    def get_normalized(self) -> Vector:
        lenght = self.get_length()
        return Vector(0, 0) \
            if lenght == 0 \
            else Vector(round(self.x / lenght, 2), round(self.y / lenght, 2))

    def angle_between(self, other: Vector) -> int:
        dot_product = self.dot(other)
        magnitude_product = self.get_length() * other.get_length()
        if magnitude_product == 0:
            return 0
        return round(math.degrees(math.acos(dot_product / magnitude_product)))

    def get_angle(self) -> int:
        y_vector = Vector(0, 1)
        dot_product = self.dot(y_vector)
        magnitude_product = self.get_length() * y_vector.get_length()
        if magnitude_product == 0:
            return 0
        return round(math.degrees(math.acos(dot_product / magnitude_product)))

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta
        return Vector(round(new_x, 2), round(new_y, 2))
