from __future__ import annotations
import math


class Vector:
    def __init__(self, x_vector: float | int, y_vector: float | int) -> None:
        self.x = round(x_vector, 2)
        self.y = round(y_vector, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> int | float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(round(self.x * other, 2),
                          round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        length_product = self.get_length() * other.get_length()
        if length_product == 0:
            return 0
        cos_angle = ((self.x * other.x + self.y * other.y)
                     / length_product)
        cos_angle = max(-1, min(1, cos_angle))
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> float | int:
        reference_vector = Vector(0, 1)
        return self.angle_between(reference_vector)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x_vector = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_vector = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(x_vector, 2), round(y_vector, 2))
