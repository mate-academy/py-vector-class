from __future__ import annotations
import math


class Vector:
    def __init__(self, vector_x: float | int, vector_y: float | int) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError("Multiplication with this type is not supported")

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float, float],
            end_point: tuple[float, float]
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, another_vector: Vector) -> float:
        dot_product = self * another_vector
        len_vector1 = self.get_length()
        len_vector2 = another_vector.get_length()
        cos_theta = dot_product / (len_vector1 * len_vector2)
        return round(math.degrees(math.acos(cos_theta)))

    def get_angle(self) -> float:
        cos_theta = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_theta)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
