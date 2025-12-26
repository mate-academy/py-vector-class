from __future__ import annotations
import math


class Vector:

    def __init__(
            self,
            coordinate_1: int | float,
            coordinate_2: int | float
    ) -> None:
        self.x = round(coordinate_1, 2)
        self.y = round(coordinate_2, 2)

    def __add__(self, other: Vector | tuple) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | tuple) -> Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        x_axis = end_point[0] - start_point[0]
        y_axis = end_point[1] - start_point[1]
        return Vector(x_axis, y_axis)

    def get_length(self) -> int | float:
        return ((self.x ** 2 + self.y ** 2)**0.5)

    def get_normalized(self) -> Vector:
        length = ((self.x ** 2 + self.y ** 2)**0.5)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other_vector: Vector) -> int | float:
        dot_product = self.x * other_vector.x + self.y * other_vector.y
        self_length = math.sqrt(self.x ** 2 + self.y ** 2)
        other_length = math.sqrt(other_vector.x ** 2 + other_vector.y ** 2)
        return round(
            math.degrees
            (math.acos(dot_product / (self_length * other_length)))
        )

    def get_angle(self) -> int | float:
        return int(abs(math.degrees(math.acos(
            self.y / math.sqrt(self.x ** 2 + self.y ** 2)
        ))))

    def rotate(self, degrees: int | float) -> Vector:
        radi = math.radians(degrees)
        cosinus = math.cos(radi)
        sinus = math.sin(radi)
        rad = [[cosinus, -sinus], [sinus, cosinus]]
        coord_1 = rad[0][0] * self.x + rad[0][1] * self.y
        coord_2 = rad[1][0] * self.x + rad[1][1] * self.y
        return Vector(coord_1, coord_2)
