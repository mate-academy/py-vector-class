from __future__ import annotations
import math


class Vector:
    def __init__(self, point_x: int | float, point_y: int | float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            point_x=self.x + other.x,
            point_y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            point_x=self.x - other.x,
            point_y=self.y - other.y
        )

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        if isinstance(other, (int, float)):
            return Vector(
                point_x=self.x * other,
                point_y=self.y * other
            )

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        start_point_list = list(start_point)
        end_point_list = list(end_point)

        return cls(
            point_x=end_point_list[0] - start_point_list[0],
            point_y=end_point_list[1] - start_point_list[1]
        )

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:

        leng = Vector.get_length(self)

        return Vector(
            point_x=self.x / leng,
            point_y=self.y / leng
        )

    def angle_between(self, vector: Vector) -> int:
        first_len = Vector.get_length(self)
        second_len = Vector.get_length(vector)
        scar_mul = self * vector
        cos = scar_mul / (first_len * second_len)
        result = math.degrees(math.acos(cos))

        return round(result)

    def get_angle(self) -> int:
        radians = math.atan2(self.x, self.y)
        result = math.degrees(radians)

        return abs(round(result))

    def rotate(self, degress: int) -> Vector:
        radians = math.radians(degress)
        point_x = math.cos(radians) * self.x - math.sin(radians) * self.y
        point_y = math.sin(radians) * self.x + math.cos(radians) * self.y

        return Vector(point_x, point_y)
