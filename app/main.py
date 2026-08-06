from __future__ import annotations
import math


class Vector:
    def __init__(self, x_point: float, y_point: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x_point=self.x + other.x, y_point=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x_point=self.x - other.x, y_point=self.y - other.y)

    def __mul__(self, other: float | Vector) -> float | Vector:
        if isinstance(other, float | int):
            return Vector(x_point=self.x * other, y_point=self.y * other)
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        return Vector(
            x_point=self.x * (1 / self.get_length()),
            y_point=self.y * (1 / self.get_length()),
        )

    def angle_between(self, vector: Vector) -> int:
        return round(
            math.degrees(
                math.acos(
                    (self * vector) / (self.get_length() * vector.get_length())
                )
            )
        )

    def get_angle(self) -> int:
        return self.angle_between(vector=Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            x_point=self.x * math.cos(math.radians(degrees))
            - self.y * math.sin(math.radians(degrees)),
            y_point=self.y * math.cos(math.radians(degrees))
            + self.x * math.sin(math.radians(degrees)),
        )
