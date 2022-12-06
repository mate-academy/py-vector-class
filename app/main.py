from __future__ import annotations
import math


class Vector:
    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(point_x=self.x + other.x,
                      point_y=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(point_x=self.x - other.x,
                      point_y=self.y - other.y)

    def __mul__(self, other: Vector) -> [float, Vector]:
        if isinstance(other, Vector):
            dot_product = (self.x * other.x) + (self.y * other.y)
            return dot_product
        return Vector(point_x=self.x * other,
                      point_y=self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> Vector:

        start_point = cls(start_point[0], start_point[1])
        end_point = cls(end_point[0], end_point[1])
        direction_vector = end_point - start_point
        return direction_vector

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            point_x=round(self.x / self.get_length(), 2),
            point_y=round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other: Vector) -> int:
        cosine = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cosine)))

    def get_angle(self) -> int:
        cos_a = self.y / self.get_length()
        angle_degrees = math.degrees(math.acos(cos_a))
        return round(angle_degrees)

    def rotate(self, degrees: int) -> Vector:
        rad = math.radians(degrees)
        x_rotate = math.cos(rad) * self.x - math.sin(rad) * self.y
        y_rotate = math.sin(rad) * self.x + math.cos(rad) * self.y
        return Vector(x_rotate, y_rotate)
