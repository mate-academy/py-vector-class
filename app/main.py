from __future__ import annotations
from typing import Union
import math


class Vector:

    Int_float = Union[int | float]

    def __init__(self, coord_x: Int_float, coord_y: Int_float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            coord_x=round(self.x + other.x, 2),
            coord_y=round(self.y + other.y, 2)
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            coord_x=round(self.x - other.x, 2),
            coord_y=round(self.y - other.y, 2)
        )

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            result = (self.x * other.x) + (self.y * other.y)
            return result
        return Vector(
            coord_x=round(self.x * other, 2),
            coord_y=round(self.y * other, 2)
        )

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_points: tuple,
                                    end_point: tuple) -> Vector:
        new_x = end_point[0] - start_points[0]
        new_y = end_point[1] - start_points[1]
        return cls(
            coord_x=new_x,
            coord_y=new_y
        )

    def get_length(self) -> float:
        length = (self.x ** 2 + self.y ** 2) ** 0.5
        return length

    def get_normalized(self) -> Vector | float:
        length = self.get_length()
        normalized_x = self.x / length
        normalized_y = self.y / length
        return Vector(
            coord_x=normalized_x,
            coord_y=normalized_y
        )

    def angle_between(self, other: Vector) -> int | float:
        dote_product = self * other
        magnitude = self.get_length() * other.get_length()
        cosine = dote_product / magnitude
        angle_in_radius = math.acos(cosine)
        angle_in_degree = math.degrees(angle_in_radius)
        return round(angle_in_degree)

    def get_angle(self) -> int | float:
        return round(abs(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:

        radians = math.radians(degrees)

        cosine = math.cos(radians)
        sine = math.sin(radians)

        rotated_x = cosine * self.x - sine * self.y
        rotated_y = sine * self.x + cosine * self.y

        return Vector(
            coord_x=rotated_x,
            coord_y=rotated_y
        )
