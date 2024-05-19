from __future__ import annotations
import math


class Vector:
    def __init__(
            self,
            coordinate_x: float | int,
            coordinate_y: float | int
    ) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                self.x + other.x,
                self.y + other.y
            )

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                self.x - other.x,
                self.y - other.y
            )

    def __mul__(
            self,
            other: int | float | Vector
    ) -> int | float | Vector:
        if isinstance(other, (int, float)):
            return Vector(
                self.x * other,
                self.y * other
            )
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length_vector = self.get_length()
        return Vector(
            self.x / length_vector,
            self.y / length_vector
        )

    def angle_between(self, other: Vector) -> int:
        if isinstance(other, Vector):
            return round(
                math.degrees(
                    math.acos(
                        self.__mul__(other)
                        / (self.get_length() * other.get_length())
                    )
                )
            )

    def get_angle(self) -> int:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            self.x * math.cos(math.radians(degrees))
            - self.y * math.sin(math.radians(degrees)),
            self.x * math.sin(math.radians(degrees))
            + self.y * math.cos(math.radians(degrees))
        )

