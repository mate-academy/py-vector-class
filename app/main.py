from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other_vector: Vector) -> Vector:
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    def __sub__(self, other_vector: Vector) -> Vector:
        return Vector(self.x - other_vector.x, self.y - other_vector.y)

    def __mul__(self, mul: float | Vector) -> Vector | float:
        if isinstance(mul, Vector):
            return self.x * mul.x + self.y * mul.y
        return Vector(self.x * mul, self.y * mul)

    @classmethod
    def create_vector_by_two_points(
            cls, first_tuple: tuple, second_tuple: tuple
    ) -> Vector:
        x_coordinate = second_tuple[0] - first_tuple[0]
        y_coordinate = second_tuple[1] - first_tuple[1]
        return cls(x_coordinate, y_coordinate)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        else:
            x_normalized = self.x / length
            y_normalized = self.y / length
            return Vector(x_normalized, y_normalized)

    def angle_between(self, other_vector: Vector) -> Vector:
        dot_product = self.x * other_vector.x + self.y * other_vector.y
        magnitude_product = self.get_length() * other_vector.get_length()

        if magnitude_product == 0:
            return 0

        cos_a = dot_product / magnitude_product
        degrees = math.degrees(math.acos(cos_a))
        return round(degrees)

    def get_angle(self) -> float:
        angle_rad = math.atan2(self.x, self.y)
        degrees = math.degrees(angle_rad)
        return abs(round(degrees))

    def rotate(self, degrees: int) -> float:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
