from __future__ import annotations
from math import sqrt, acos, degrees, radians, cos, sin


class Vector:
    def __init__(self, x_cor: float, y_cor: float) -> None:
        self.x = round(x_cor, 2)
        self.y = round(y_cor, 2)

    def __str__(self) -> str:
        return f"Vector ({self.x}, {self.y})"

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_cor=self.x + other.x,
            y_cor=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_cor=self.x - other.x,
            y_cor=self.y - other.y
        )

    def __mul__(self, other: Vector | float) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            x_cor=self.x * other,
            y_cor=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[float, float],
                                    end_point: tuple[float, float]) -> Vector:
        return cls(
            x_cor=end_point[0] - start_point[0],
            y_cor=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            x_cor=self.x / self.get_length(),
            y_cor=self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        cosine = self * other / (self.get_length() * other.get_length())
        return round(degrees(acos(cosine)))

    def get_angle(self) -> int:
        return round(degrees(acos(self.y / self.get_length())))

    def rotate(self, angle: float) -> Vector:
        return Vector(
            x_cor=self.x * cos(radians(angle)) - self.y * sin(radians(angle)),
            y_cor=self.x * sin(radians(angle)) + self.y * cos(radians(angle))
        )
