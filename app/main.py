from __future__ import annotations
import math
# import numpy as np


class Vector:
    # write your code here
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, vector3: "Vector" | float | int) -> Vector:
        if isinstance(vector3, Vector):
            return Vector(self.x + vector3.x, self.y + vector3.y)
        else:
            return Vector(self.x + vector3, self.y + vector3)

    def __sub__(self, vector3: Vector | float | int) -> Vector:
        if isinstance(vector3, Vector):
            return Vector(self.x - vector3.x, self.y - vector3.y)
        else:
            return Vector(self.x - vector3, self.y - vector3)

    def __mul__(self, vector_product: Vector | int | float) -> float | Vector:
        if isinstance(vector_product, Vector):
            return self.x * vector_product.x + self.y * vector_product.y
        elif isinstance(vector_product, (int, float)):
            return Vector(self.x * vector_product, self.y * vector_product)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> float:
        if len(start_point) != len(end_point):
            raise ValueError("Tuples must be the same dimension")
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]
        return cls(new_x, new_y)

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        magnitude_v = math.sqrt(self.x ** 2 + self.y ** 2)
        return Vector(self.x / magnitude_v, self.y / magnitude_v)

    def angle_between(self, vector2: Vector) -> int:
        dot_product = (self.x * vector2.x) + (self.y * vector2.y)
        denominator = self.get_length() * vector2.get_length()

        if denominator == 0:
            return 0

        cos_theta = max(-1.0, min(1.0, dot_product / denominator))
        radians = math.acos(cos_theta)
        return int(round(math.degrees(radians)))

    def get_angle(self) -> int:
        mag_angle = math.hypot(self.x, self.y)
        if mag_angle == 0:
            return 0
        cos_theta = self.y / mag_angle
        cos_theta = max(-1.0, min(1.0, cos_theta))

        angle = math.degrees(math.acos(cos_theta))

        return int(round(angle))

    def rotate(self, degrees: int) -> Vector:
        cos_theta = math.cos(math.radians(degrees))
        sin_theta = math.sin(math.radians(degrees))
        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta
        return Vector(new_x, new_y)
