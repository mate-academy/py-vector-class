from typing import Any
import math


class Vector:

    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Any) -> Any:
        vector = Vector(self.x + other.x, self.y + other.y)
        return vector

    def __sub__(self, other: Any) -> Any:
        vector = Vector(self.x - other.x, self.y - other.y)
        return vector

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, (int, float)):
            vector = Vector(self.x * other.real, self.y * other.real)
            return vector
        else:
            dot_product = self.x * other.x + self.y * other.y
            return dot_product

    @classmethod
    def create_vector_by_two_points(
        cls, point_1: tuple,
        point_2: tuple
    ) -> Any:
        vector = cls(point_2[0] - point_1[0], point_2[1] - point_1[1])
        return vector

    def get_length(self) -> float:
        length = (self.x**2 + self.y**2)**0.5
        return length

    def get_normalized(self) -> float:
        vector = Vector(
            self.x
            / Vector.get_length(self), self.y
            / Vector.get_length(self))
        return vector

    def angle_between(self, other: Any) -> float:
        dot_product = self * other
        length_1 = Vector.get_length(self)
        length_2 = Vector.get_length(other)
# we find out the cosine
        angle = dot_product / (length_1 * length_2)
# find arccosine
        angle = math.acos(angle)
# find the rounded degree of the angle
        angle = round(math.degrees(angle))
        return angle

    def get_angle(self) -> int:
        vector_oy = Vector(0, 1)
        angle = Vector.angle_between(self, vector_oy)
        return angle

    def rotate(self, degree: int) -> Any:
        radian = math.radians(degree)
        rotated_x = self.x * math.cos(radian) - self.y * math.sin(radian)
        rotated_y = self.x * math.sin(radian) + self.y * math.cos(radian)
        rotate_vector = Vector(rotated_x, rotated_y)
        return rotate_vector
