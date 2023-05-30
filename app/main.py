from __future__ import annotations
import math


class Vector:
    def __init__(self, x_point: int | float, y_point: int | float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            round(self.x + other.x, 2),
            round(self.y + other.y, 2)
        )

    def __sub__(self, other: Vector | int | float) -> Vector:
        x_point = other.x if isinstance(other, Vector) else other
        y_point = other.y if isinstance(other, Vector) else other

        return Vector(
            round(self.x - x_point, 2),
            round(self.y - y_point, 2)
        )

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        if isinstance(other, int) or isinstance(other, float):
            return Vector(
                round(self.x * other, 2),
                round(self.y * other, 2)
            )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[int | float],
            end_point: tuple[int | float]
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[-1] - start_point[-1]
        )

    def get_length(self) -> int | float:
        return ((self.x ** 2) + (self.y ** 2)) ** .5

    def get_normalized(self) -> Vector:
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other: Vector) -> int:
        angle = (self.__mul__(other)
                 / (self.get_length()
                    * other.get_length()))

        return round(math.degrees(math.acos(angle)))

    def get_angle(self) -> int:
        positive_y = Vector(0, 1)

        angle = (self.__mul__(positive_y)
                 / (self.get_length()
                    * positive_y.get_length()))

        return round(math.degrees(math.acos(angle)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)

        return Vector(
            self.x * math.cos(radians) - self.y * math.sin(radians),
            self.x * math.sin(radians) + self.y * math.cos(radians)
        )
