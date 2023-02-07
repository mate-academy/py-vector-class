from __future__ import annotations
import math


class Vector:
    def __init__(self,
                 point_x: float,
                 point_y: float) -> callable:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            point_x=self.x + other.x,
            point_y=self.y + other.y,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            point_x=self.x - other.x,
            point_y=self.y - other.y
        )

    def __mul__(self, other: float | int | Vector) -> Vector | float:
        if isinstance(other, Vector):
            dot_product = (self.x * other.x) + (self.y * other.y)
            return dot_product
        return Vector(
            point_x=self.x * other,
            point_y=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        point_x = round(end_point[0] - start_point[0], 2)
        point_y = round(end_point[1] - start_point[1], 2)
        return Vector(point_x, point_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + (self.y ** 2))

    def get_normalized(self) -> Vector:
        point_x = round(self.x / Vector.get_length(self), 2)
        point_y = round(self.y / Vector.get_length(self), 2)
        return Vector(point_x, point_y)

    def angle_between(self, vector: float | int) -> Vector | float:
        length_self = Vector.get_length(self)
        length_vector = Vector.get_length(vector)
        product_length = length_self * length_vector
        cos_a = self.__mul__(vector) / product_length
        corner = math.degrees(math.acos(cos_a))
        return round(corner)

    def get_angle(self) -> Vector:
        corner_y = Vector(0, abs(self.y))
        return self.angle_between(corner_y)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        point_x = round(self.x * cos_a - self.y * sin_a, 2)
        point_y = round(self.x * sin_a + self.y * cos_a, 2)
        return Vector(point_x, point_y)
