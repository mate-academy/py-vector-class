from __future__ import annotations
from math import sqrt, degrees, acos, sin, radians, cos


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other: (Vector, float)) -> Vector:
        if isinstance(other, (float, int)):
            return Vector(
                x=self.x * other,
                y=self.y * other
            )
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        vector = cls(end_point[0] - start_point[0],
                     end_point[1] - start_point[1])

        return vector

    def get_length(self) -> float:
        return sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> Vector:
        normalized_x = self.x / self.get_length()
        normalized_y = self.y / self.get_length()

        return Vector(normalized_x, normalized_y)

    def angle_between(self, vector: Vector) -> float:
        scalar_product = (self.x * vector.x) + (self.y * vector.y)
        vector_modules = sqrt((self.x ** 2) + (self.y ** 2)) * sqrt(
            vector.x ** 2 + vector.y ** 2)

        return round(degrees(acos(scalar_product / vector_modules)))

    def get_angle(self) -> float:
        vector_y = Vector(0, 1)
        return self.angle_between(vector_y)

    def rotate(self, degrees: int | float) -> Vector:
        rad = radians(degrees)
        rotated_x = self.x * cos(rad) - self.y * sin(rad)
        rotated_y = self.x * sin(rad) + self.y * cos(rad)

        return Vector(rotated_x, rotated_y)
