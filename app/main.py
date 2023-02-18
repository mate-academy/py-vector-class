from __future__ import annotations
from math import acos, cos, degrees, radians, sin, sqrt


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            abscissa_addition = round(self.x + other.x, 2)
            ordinate_addition = round(self.y + other.y, 2)

            return Vector(abscissa_addition, ordinate_addition)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            abscissa_subtraction = round(self.x - other.x, 2)
            ordinate_subtraction = round(self.y - other.y, 2)

            return Vector(abscissa_subtraction, ordinate_subtraction)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            abscissa_multiplication = self.x * other.x
            ordinate_multiplication = self.y * other.y
            dot_product = abscissa_multiplication + ordinate_multiplication

            return dot_product

        abscissa_multiplication = round(self.x * other, 2)
        ordinate_multiplication = round(self.y * other, 2)

        return Vector(abscissa_multiplication, ordinate_multiplication)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        abscissa_coordinate = end_point[0] - start_point[0]
        ordinate_coordinate = end_point[1] - start_point[1]

        return cls(x=abscissa_coordinate, y=ordinate_coordinate)

    def get_length(self) -> float:
        vector_length = sqrt(self.x ** 2 + self.y ** 2)

        return vector_length

    def get_normalized(self) -> Vector:
        abscissa_normalized = round(self.x / self.get_length(), 2)
        ordinate_normalized = round(self.y / self.get_length(), 2)

        return Vector(abscissa_normalized, ordinate_normalized)

    def angle_between(self, vector: Vector) -> int:
        dot_product = self * vector
        product_of_lengths = self.get_length() * vector.get_length()
        angle_cosine = dot_product / product_of_lengths
        angle = round(degrees(acos(angle_cosine)))

        return angle

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degree: int) -> Vector:
        radian = radians(degree)
        cosine_angle = cos(radian)
        sine_angle = sin(radian)
        abscissa = cosine_angle * self.x - sine_angle * self.y
        ordinate = sine_angle * self.x + cosine_angle * self.y

        return Vector(abscissa, ordinate)
