from __future__ import annotations

from math import sqrt, degrees, acos, radians, cos, sin, atan2, pi
from typing import Union


class Vector:
    def __init__(
            self,
            coordinate_x: Union[int, float],
            coordinate_y: Union[int, float]
    ) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other_vector: Vector) -> Vector:
        new_x = round(self.x + other_vector.x, 2)
        new_y = round(self.y + other_vector.y, 2)
        return Vector(new_x, new_y)

    def __sub__(self, other_vector: Vector) -> Vector:
        new_x = round(self.x - other_vector.x, 2)
        new_y = round(self.y - other_vector.y, 2)
        return Vector(new_x, new_y)

    def __mul__(
            self,
            other_vector: Union[Vector, float, int]
    ) -> Union[Vector, float]:
        if isinstance(other_vector, (float, int)):
            new_x = self.x * other_vector
            new_y = self.y * other_vector
            return Vector(new_x, new_y)
        else:
            dot_product = self.x * other_vector.x + self.y * other_vector.y
            return dot_product

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        vector_x = round(end_point[0] - start_point[0], 2)
        vector_y = round(end_point[1] - start_point[1], 2)

        return cls(vector_x, vector_y)

    def get_length(self) -> float:
        get_len_result = sqrt(self.x ** 2 + self.y ** 2)
        return get_len_result

    def get_normalized(self) -> Vector:
        lenght_vector = self.get_length()
        self.x = round(self.x / lenght_vector, 2)
        self.y = round(self.y / lenght_vector, 2)

        return Vector(self.x, self.y)

    def angle_between(self, other_vector: Vector) -> float:
        dot_product = self * other_vector
        magnitude1 = sqrt(self.x ** 2 + self.y ** 2)
        magnitude2 = sqrt(other_vector.x ** 2 + other_vector.y ** 2)
        cos_theta = dot_product / (magnitude1 * magnitude2)
        angle_rad = acos(cos_theta)
        angle_deg = angle_rad * 180 / pi
        angle_deg = round(angle_deg)

        return angle_deg

    def get_angle(self) -> float:
        angle_rad = atan2(self.x, self.y)
        angle_deg = degrees(angle_rad)

        return abs(round(angle_deg))

    def rotate(self, degrees_for_rotate: int) -> Vector:
        degree_to_radian = radians(degrees_for_rotate)
        cos_angle = cos(degree_to_radian)
        sin_angle = sin(degree_to_radian)
        x_new = round(self.x * cos_angle - self.y * sin_angle, 2)
        y_new = round(self.x * sin_angle + self.y * cos_angle, 2)
        return Vector(x_new, y_new)
