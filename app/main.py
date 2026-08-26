from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x, self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x, self.y - other.y
        )

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, int | float):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        end_x = end_point[0] - start_point[0]
        end_y = end_point[1] - start_point[1]
        return cls(end_x, end_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        lenth = math.sqrt(self.x ** 2 + self.y ** 2)
        if lenth == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        norm_x = self.x / lenth
        norm_y = self.y / lenth
        return Vector(norm_x, norm_y)

    def angle_between(self, other: Vector) -> int:
        dot_prod = self * other
        len_self = self.get_length()
        len_other = other.get_length()
        angle = math.degrees(math.acos(dot_prod / (len_self * len_other)))
        return round(angle)

    def get_angle(self) -> int | int:
        len_self = self.get_length()
        if self.x == 0:
            return 0
        elif self.y > 0:
            angle = math.degrees(math.asin(abs(self.x) / len_self))
            return round(angle)
        elif self.y < 0:
            angle = math.degrees(math.asin(abs(self.y) / len_self))
            return round(angle) + 90
        else:
            return 90

    def rotate(self, degrees: int) -> Vector:
        sin_degree = math.sin(math.radians(degrees))
        cos_degree = math.cos(math.radians(degrees))
        rotated_x = self.x * cos_degree - self.y * sin_degree
        rotated_y = self.x * sin_degree + self.y * cos_degree
        return Vector(rotated_x, rotated_y)
