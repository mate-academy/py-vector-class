from __future__ import annotations
import math


class Vector:

    def __init__(self, dot_x: float, dot_y: float) -> None:
        self.x = round(dot_x, 2)
        self.y = round(dot_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            dot_x=self.x + other.x,
            dot_y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            dot_x=self.x - other.x,
            dot_y=self.y - other.y
        )

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(dot_x=self.x * other, dot_y=self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / Vector.get_length(self),
            self.y / Vector.get_length(self)
        )

    def angle_between(self, vector: Vector) -> int:
        return math.ceil(
            math.degrees(math.acos(self.__mul__(vector)
                                   / (Vector.get_length(self)
                                      * Vector.get_length(vector))))
        )

    def get_angle(self) -> float:
        return round(abs(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos = math.cos(radians)
        sin = math.sin(radians)
        dot_x = self.x * cos - self.y * sin
        dot_y = self.x * sin + self.y * cos
        return Vector(dot_x, dot_y)
