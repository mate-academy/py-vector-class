from __future__ import annotations
import math


class Vector:
    def __init__(
        self,
        x: float, # noqa: VNE001 E261
        y: float # noqa: VNE001 E261
    ) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        if isinstance(other, int | float):
            return Vector(self.x * other, self.y * other)

    def get_length(self) -> float:
        return math.sqrt(
            (self.x ** 2)
            + (self.y ** 2)
        )

    def get_normalized(self) -> Vector:
        return self * (1 / self.get_length())

    def angle_between(self, vector: Vector) -> int:
        cos_a = (
            (self * vector)
            / (self.get_length() * vector.get_length())
        )
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        tan_a = abs(self.x) / abs(self.y)
        angle = round(math.degrees(math.atan(tan_a)))
        if self.y < 0:
            return 180 - angle
        return angle

    def rotate(self, degrees: int) -> Vector:
        sin_b = math.sin(math.radians(degrees))
        cos_b = math.cos(math.radians(degrees))
        return Vector(
            (cos_b * self.x) - (sin_b * self.y),
            (sin_b * self.x) + (cos_b * self.y)
        )

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[int | float, int | float],
        end_point: tuple[int | float, int | float]
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )
