from __future__ import annotations
import math


class Vector:
    def __init__(
            self, x_coordinate: int | float,
            y_coordinate: int | float
    ) -> None:
        self.x_coordinate = round(x_coordinate, 2)
        self.y_coordinate = round(y_coordinate, 2)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x_coordinate - other.x_coordinate,
            self.y_coordinate - other.y_coordinate
        )

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x_coordinate + other.x_coordinate,
            self.y_coordinate + other.y_coordinate
        )

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, (int, float)):
            return Vector(
                round(self.x_coordinate * other, 2),
                round(self.y_coordinate * other, 2)
            )

        if isinstance(other, Vector):
            return (self.x_coordinate * other.x_coordinate
                    + self.y_coordinate * other.y_coordinate)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(
            round(self.x_coordinate / length, 2),
            round(self.y_coordinate / length, 2)
        )

    def get_length(self) -> float | int:
        return math.sqrt(self.x_coordinate ** 2
                         + self.y_coordinate ** 2)

    def angle_between(self, other: Vector) -> float | int:
        dot_product = self * other
        cos_a = dot_product / (self.get_length() * other.get_length())
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self) -> int:
        other = Vector(0, 1)
        return self.angle_between(other)

    def rotate(self, degrees: int) -> Vector:
        x_coordinate = (math.cos(math.radians(degrees)) * self.x_coordinate
                        - math.sin(math.radians(degrees)) * self.y_coordinate)
        y_coordinate = (math.sin(math.radians(degrees)) * self.x_coordinate
                        + math.cos(math.radians(degrees)) * self.y_coordinate)
        return Vector(x_coordinate, y_coordinate)
