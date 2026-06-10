from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )

    def __mul__(self, other: Vector | float) -> Vector | float:

        if isinstance(other, Vector):
            return (self.x * other.x) + (
                self.y * other.y
            )
        else:
            return Vector(
                round(self.x * other, 2),
                round(self.y * other, 2)
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
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: Vector) -> int:

        cos_a = (
            self.x * vector.x
            + self.y * vector.y
        ) / (self.get_length() * vector.get_length())

        angle = math.degrees(math.acos(cos_a))

        return round(angle)

    def get_angle(self) -> int:
        angle = math.degrees(math.atan2(self.x, self.y))

        return round(abs(angle))

    def rotate(self, degrees: int) -> Vector:

        radians = math.radians(degrees)
        return Vector(
            self.x * math.cos(radians)
            - self.y * math.sin(radians),
            self.x * math.sin(radians)
            + self.y * math.cos(radians),
        )
