from __future__ import annotations
import math


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

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
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def get_normalized(self) -> Vector:
        return (
            Vector(
                self.x / self.get_length(),
                self.y / self.get_length()
            )
        )

    def angle_between(self, other: Vector) -> int:
        cos_a = self.__mul__(other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        positive_y_axis = Vector(0, 1)
        return self.angle_between(positive_y_axis)

    def rotate(self, degrees: int) -> Vector:
        return (
            Vector(
                self.x * math.cos(math.radians(degrees))
                - self.y * math.sin(math.radians(degrees)),
                self.x * math.sin(math.radians(degrees))
                + self.y * math.cos(math.radians(degrees))
            )
        )
