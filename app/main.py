from __future__ import annotations
from math import sqrt, degrees, acos, cos, sin, radians


class Vector:

    def __init__(self, value_x: float, value_y: float) -> None:
        self.x = round(value_x, 2)
        self.y = round(value_y, 2)

    def __repr__(self) -> str:
        return f"Vector({self.x} : {self.y})"

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        elif isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple(float),
        end_point: tuple(float)
    ) -> Vector:
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]

        return cls(new_x, new_y)

    def get_length(self) -> float:
        length = sqrt(self.x ** 2 + self.y ** 2)

        return length

    def get_normalized(self) -> Vector:
        length = self.get_length()
        new_x = round(self.x / length, 2)
        new_y = round(self.y / length, 2)

        return Vector(new_x, new_y)

    def get_cosine(self, other: Vector) -> float:
        length_self = self.get_length()
        length_other = other.get_length()
        dot_product = self * other

        return dot_product / (length_self * length_other)

    def angle_between(self, other: Vector) -> int:

        cos_a = self.get_cosine(other)
        angle = degrees(acos(cos_a))

        return round(angle)

    def get_angle(self) -> int:
        pos_y_vector = Vector(0, abs(self.y))

        return self.angle_between(pos_y_vector)

    def rotate(self, degree: int) -> Vector:

        rad_degree = radians(degree)
        new_x = cos(rad_degree) * self.x - sin(rad_degree) * self.y
        new_y = sin(rad_degree) * self.x + cos(rad_degree) * self.y

        return Vector(new_x, new_y)
