from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coo: int | float, y_coo: int | float) -> None:
        self.x = round(x_coo, 2)
        self.y = round(y_coo, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coo=self.x + other.x,
            y_coo=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_coo=self.x - other.x,
            y_coo=self.y - other.y
        )

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, (int, float)):
            return Vector(
                x_coo=self.x * other,
                y_coo=self.y * other
            )
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            x_coo=end_point[0] - start_point[0],
            y_coo=end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            x_coo=self.x / self.get_length(),
            y_coo=self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        cos_a = self.__mul__(other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> Vector:
        rad = math.radians(degrees)
        return Vector(
            x_coo=math.cos(rad) * self.x - math.sin(rad) * self.y,
            y_coo=math.sin(rad) * self.x + math.cos(rad) * self.y
        )
