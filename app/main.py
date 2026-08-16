from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:# noqa VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                x=self.x + other.x,
                y=self.y + other.y
            )

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                x=self.x - other.x,
                y=self.y - other.y
            )

    def __mul__(self, other: Vector | int | float) -> Vector | float :
        if isinstance(other, Vector):
            return (self.x * other.x + self.y * other.y)
        else:
            return Vector(
                x=self.x * other,
                y=self.y * other
            )

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> Vector:
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(
            x=self.x / length,
            y=self.y / length
        )

    def angle_between(self, vector: "Vector") -> int:
        cos_a = (self * vector) / (self.get_length() * vector.get_length())
        degrees = math.degrees(math.acos(cos_a))
        return round(degrees)

    def get_angle(self) -> int:
        cos_a = self.y / self.get_length()
        degrees = math.degrees(math.acos(cos_a))
        return round(degrees)

    def rotate(self, degrees: int) -> Vector:
        angle = math.radians(degrees)
        return Vector(
            x=self.x * math.cos(angle) - self.y * math.sin(angle),
            y=self.x * math.sin(angle) + self.y * math.cos(angle)
        )
