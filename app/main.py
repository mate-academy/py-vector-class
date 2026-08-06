from __future__ import annotations
import math


class Vector:
    def __init__(self, x_cor: float, y_cor: float) -> None:
        self.x = round(x_cor, 2)
        self.y = round(y_cor, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> int | float | Vector:
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
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x * (1 / self.get_length()),
            self.y * (1 / self.get_length()))

    def angle_between(self, vector2: Vector) -> int:
        return int(round(
            math.degrees(math.acos(
                (self * vector2) / (self.get_length() * vector2.get_length())
            ))
        ))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 10))

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            math.cos(
                math.radians(degrees)
            ) * self.x - math.sin(
                math.radians(degrees)
            ) * self.y,
            math.sin(
                math.radians(degrees)
            ) * self.x + math.cos(
                math.radians(degrees)
            ) * self.y
        )
