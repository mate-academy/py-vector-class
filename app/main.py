from __future__ import annotations
import math


class Vector:

    def __init__(self, x_point: float, y_point: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            round(self.x + other.x, 2),
            round(self.y + other.y, 2)
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            round(self.x - other.x, 2),
            round(self.y - other.y, 2)
        )

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(
            round(self.x * other, 2),
            round(self.y * other, 2)
        )

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            round(end_point[0] - start_point[0], 2),
            round(end_point[1] - start_point[1], 2)
        )

    def get_length(self) -> float:
        return pow(self.x ** 2 + self.y ** 2, 0.5)

    def get_normalized(self) -> Vector:
        len_vector = self.get_length()
        return Vector(
            round(self.x / len_vector, 2),
            round(self.y / len_vector, 2)
        )

    def angle_between(self, other: Vector) -> math.degrees:
        length1 = self.get_length()
        length2 = other.get_length()
        scalar_product = self.__mul__(other)
        acos = math.acos(scalar_product / (length1 * length2))
        return round(math.degrees(acos))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        theta = math.radians(degrees)
        cos = math.cos(theta)
        sin = math.sin(theta)
        x_point = self.x * cos - self.y * sin
        y_point = self.x * sin + self.y * cos
        return Vector(round(x_point, 2), round(y_point, 2))
