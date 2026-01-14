from __future__ import annotations
import math


class Vector:

    def __init__(self, x_cord: int, y_cord: int) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float) -> Vector:
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        result_x = end_point[0] - start_point[0]
        result_y = end_point[1] - start_point[1]
        return cls(result_x, result_y)

    def get_length(self) -> int:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        result_x = round(self.x / self.get_length(), 2)
        result_y = round(self.y / self.get_length(), 2)
        return Vector(result_x, result_y)

    def angle_between(self, vector: Vector) -> int:
        skalyar = self.x * vector.x + self.y * vector.y
        length_of_module_a = math.sqrt(self.x ** 2 + self.y ** 2)
        length_of_module_b = math.sqrt(vector.x ** 2 + vector.y ** 2)
        cos_a = skalyar / (length_of_module_a * length_of_module_b)
        result = math.degrees(math.acos(cos_a))
        return round(result)

    def get_angle(self) -> int:
        positive_vector_y = Vector(0, 1)
        return self.angle_between(positive_vector_y)

    def rotate(self, degrees: int) -> Vector:
        cos = math.cos(math.radians(degrees))
        sin = math.sin(math.radians(degrees))
        result_x = self.x * cos - self.y * sin
        result_y = self.x * sin + self.y * cos
        return Vector(result_x, result_y)
