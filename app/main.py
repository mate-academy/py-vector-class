from __future__ import annotations
from math import sqrt, degrees, acos, atan2, radians, cos, sin


class Vector:
    def __init__(self, x: float, y: float) -> None:  # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(
            x=self.x * other,
            y=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float]
    ) -> Vector:
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        return Vector(
            x=self.x / self.get_length(),
            y=self.y / self.get_length()
        )

    def angle_between(self, vector: Vector) -> int:
        return round(
            degrees(
                acos(
                    (self.__mul__(vector))
                    / (self.get_length() * vector.get_length())
                )
            )
        )

    def get_angle(self) -> int:
        return round(abs(degrees(atan2(self.x, self.y))))

    def rotate(self, degrees: float) -> Vector:
        radians_value = radians(degrees)

        return Vector(
            x=self.x * cos(radians_value) - self.y * sin(radians_value),
            y=self.x * sin(radians_value) + self.y * cos(radians_value)
        )
