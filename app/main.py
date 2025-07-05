from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x=self.x - other.x, y=self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(x=self.x * other, y=self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple,
                                    ) -> Vector:
        return Vector(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = Vector.get_length(self)
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(
            x=self.x / length,
            y=self.y / length,
        )

    def angle_between(self, other: Vector) -> int:
        len_self = Vector.get_length(self)
        len_other = Vector.get_length(other)
        if len_self == 0 or len_other == 0:
            raise ValueError("Cannot compute angle with zero-length vector")

        cos_theta = (self * other) / (len_self * len_other)
        cos_theta = max(-1.0, min(1.0, cos_theta))
        return round(math.degrees(math.acos(cos_theta)))

    def get_angle(self) -> int:
        return Vector.angle_between(self, Vector(x=0, y=1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        return Vector(
            x=self.x * cos_theta - self.y * sin_theta,
            y=self.x * sin_theta + self.y * cos_theta,
        )
