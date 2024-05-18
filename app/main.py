from __future__ import annotations
import math


class Vector:

    def __init__(self, vector_x: float, vector_y: float) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            vector_x=self.x + other.x,
            vector_y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            vector_x=self.x - other.x,
            vector_y=self.y - other.y
        )

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(
            vector_x=round(self.x * other, 2),
            vector_y=round(self.y * other, 2)
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            vector_x=end_point[0] - start_point[0],
            vector_y=end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return abs(math.sqrt(self.x ** 2 + self.y ** 2))

    def get_normalized(self) -> Vector:
        return Vector(
            vector_x=self.x / self.get_length(),
            vector_y=self.y / self.get_length()
        )

    def angle_between(self, another: Vector) -> int:
        return round(
            math.acos(
                (self.x * another.x + self.y * another.y)
                / (self.get_length() * another.get_length())
            )
            * (180 / math.pi)
        )

    def get_angle(self) -> int:
        return round(
            math.acos(self.y / math.sqrt(self.x ** 2 + self.y ** 2))
            * (180 / math.pi)
        )

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            vector_x=(self.x
                      * math.cos(degrees * (math.pi / 180))
                      - self.y
                      * math.sin(degrees * (math.pi / 180))),
            vector_y=(self.y
                      * math.cos(degrees * (math.pi / 180))
                      + self.x
                      * math.sin(degrees * (math.pi / 180)))
        )
