from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float | int, y_coord: float | int) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
        self,
        other: Vector | int | float
    ) -> Vector | float | int | None:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return None

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float]
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot = self.x * other.x + self.y * other.y
        len1 = self.get_length()
        len2 = other.get_length()
        if len1 * len2 == 0:
            return 0
        cos_theta = dot / (len1 * len2)
        cos_theta = min(1, max(-1, cos_theta))
        degrees = math.degrees(math.acos(cos_theta))
        return int(round(degrees))

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            return 0

        cos_theta = self.y / length
        cos_theta = max(-1, min(1, cos_theta))

        degree = math.degrees(math.acos(cos_theta))
        return int(round(degree))

    def rotate(self, degrees: int | float) -> Vector:
        rad = math.radians(degrees)
        return Vector(
            self.x * math.cos(rad) - self.y * math.sin(rad),
            self.x * math.sin(rad) + self.y * math.cos(rad)
        )
