from __future__ import annotations
import math


class Vector:
    def __init__(self, x_point: int | float, y_point: int | float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __repr__(self) -> str:
        return f"Vector x:{self.x} y:{self.y}"

    def __add__(self, other: Vector) -> Vector:
        return Vector(x_point=self.x + other.x, y_point=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x_point=self.x - other.x, y_point=self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, int | float):
            return Vector(
                x_point=round(self.x * other, 2),
                y_point=round(self.y * other, 2)
            )
        dot_product = self.x * other.x + self.y * other.y
        return dot_product

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            x_point=end_point[0] - start_point[0],
            y_point=end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            x_point=round(self.x / self.get_length(), 2),
            y_point=round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other: Vector) -> int:
        angle = self.__mul__(other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(angle)))

    def get_angle(self) -> int:
        zero_x_vector = Vector(0, abs(self.y))
        length = self.get_length() * zero_x_vector.get_length()
        cos_a = self.__mul__(zero_x_vector) / length

        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, angle: int) -> Vector:
        return Vector(
            x_point=(math.cos(math.radians(angle)) * self.x)
            - (math.sin(math.radians(angle)) * self.y),
            y_point=(math.sin(math.radians(angle)) * self.x)
            + (math.cos(math.radians(angle)) * self.y)
        )
