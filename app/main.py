from __future__ import annotations
import math
from typing import Any


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector" | int | float) -> Any:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        x_coordinate = end_point[0] - start_point[0]
        y_coordinate = end_point[1] - start_point[1]
        return cls(x_coordinate, y_coordinate)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def get_normalized(self) -> Vector:
        normalized_x = self.x / self.get_length()
        normalized_y = self.y / self.get_length()
        return Vector(normalized_x, normalized_y)

    def angle_between(self, vector: Vector) -> float:
        dot_product = self.__mul__(vector)
        product_of_lengths = self.get_length() * vector.get_length()
        if -1 <= dot_product / product_of_lengths <= 1:
            return round(math.degrees
                         (math.acos
                          (dot_product / product_of_lengths)))
        else:
            if dot_product / product_of_lengths > 1:
                return 0
            else:
                return math.pi

    def get_angle(self) -> float:
        dot_product = self.x * 0 + self.y * 1
        magnitude = self.get_length()
        angle_radians = math.acos(dot_product / magnitude)
        return round(math.degrees(angle_radians))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(new_x, new_y)
