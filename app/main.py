from __future__ import annotations
import math


class Vector:

    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float | int:
        if isinstance(other, Vector):
            return (self.x * other.x + self.y * other.y)
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[-1] - start_point[-1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )

    def angle_between(self, vector: Vector) -> int | float:
        dot_p = (self.x * vector.x + self.y * vector.y)
        mag_s = (self.x ** 2 + self.y ** 2) ** 0.5
        mag_v = (vector.x ** 2 + vector.y ** 2) ** 0.5
        mag_p = mag_s * mag_v
        cos_a = dot_p / mag_p
        angle_in_radians = math.acos(cos_a)
        angle_in_degrees = round(math.degrees(angle_in_radians))
        return angle_in_degrees

    def get_angle(self) -> int:
        return -(int(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            self.x * math.cos(math.radians(degrees))
            - self.y * math.sin(math.radians(degrees)),
            self.x * math.sin(math.radians(degrees))
            + self.y * math.cos(math.radians(degrees))
        )
