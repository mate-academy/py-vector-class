from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x_coordinate = round(x_coordinate, 2)
        self.y_coordinate = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x_coordinate + other.x_coordinate,
            self.y_coordinate + other.y_coordinate,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x_coordinate - other.x_coordinate,
            self.y_coordinate - other.y_coordinate,
        )

    def __mul__(self, other: Vector | float) -> Vector | float:

        if isinstance(other, Vector):
            return (self.x_coordinate * other.x_coordinate) + (
                self.y_coordinate * other.y_coordinate
            )
        else:
            return Vector(
                round(self.x_coordinate * other, 2),
                round(self.y_coordinate * other, 2)
            )

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(end_point[0]
                   - start_point[0],
                   end_point[1]
                   - start_point[1]
                   )

    def get_length(self) -> float:
        return (self.x_coordinate**2 + self.y_coordinate**2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x_coordinate / length, self.y_coordinate / length)

    def angle_between(self, vector: Vector) -> int:

        cos_a = (
            self.x_coordinate * vector.x_coordinate
            + self.y_coordinate * vector.y_coordinate
        ) / (self.get_length() * vector.get_length())

        angle = math.degrees(math.acos(cos_a))

        return round(angle)

    def get_angle(self) -> int:
        angle = math.degrees(math.atan2(self.x_coordinate, self.y_coordinate))

        return round(abs(angle))

    def rotate(self, degrees: int) -> Vector:

        radians = math.radians(degrees)
        return Vector(
            self.x_coordinate * math.cos(radians)
            - self.y_coordinate * math.sin(radians),
            self.x_coordinate * math.sin(radians)
            + self.y_coordinate * math.cos(radians),
        )
