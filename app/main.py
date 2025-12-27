from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coor: int | float, y_coor: int | float) -> None:
        self.x = round(x_coor, 2)
        self.y = round(y_coor, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x_coor=self.x + other.x, y_coor=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x_coor=self.x - other.x, y_coor=self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> int | float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(x_coor=self.x * other, y_coor=self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            x_coor=end_point[0] - start_point[0],
            y_coor=end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(x_coor=self.x / length, y_coor=self.y / length)

    def angle_between(self, other: Vector) -> int | float:
        dot_product = self * other
        length_product = self.get_length() * other.get_length()
        radians = math.acos(dot_product / length_product)
        return round(math.degrees(radians))

    def get_angle(self) -> int:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(
            x_coor=self.x * math.cos(radians) - self.y * math.sin(radians),
            y_coor=self.x * math.sin(radians) + self.y * math.cos(radians)
        )
