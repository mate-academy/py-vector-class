from __future__ import annotations
import math


class Vector:
    def __init__(self, x_point: int | float, y_point: int | float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            x_point=self.x / Vector(self.x, self.y).get_length(),
            y_point=self.y / Vector(self.x, self.y).get_length()
        )

    def angle_between(self, other: Vector) -> int | float:
        coordinates_vector_a = (self.x ** 2 + self.y ** 2) ** 0.5
        coordinates_vector_b = (other.x ** 2 + other.y ** 2) ** 0.5
        return round(math.degrees(
            math.acos(
                self.__mul__(other)
                / (coordinates_vector_a * coordinates_vector_b))))

    def get_angle(self) -> int | float:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: int | float) -> Vector:
        rad = math.radians(degrees)
        return Vector(
            x_point=math.cos(rad) * self.x - math.sin(rad) * self.y,
            y_point=math.sin(rad) * self.x + math.cos(rad) * self.y,
        )
