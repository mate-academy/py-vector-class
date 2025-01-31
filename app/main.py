from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:  # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(
            self,
            other_coord: tuple[float, float]
    ) -> Vector:
        return Vector(self.x + other_coord.x, self.y + other_coord.y)

    def __sub__(
            self,
            other_coord: tuple[float, float]
    ) -> Vector:
        return Vector(self.x - other_coord.x, self.y - other_coord.y)

    def __mul__(self, other_coord: tuple[float, float]) -> float | Vector:
        if isinstance(other_coord, Vector):
            return self.x * other_coord.x + self.y * other_coord.y
        else:
            return Vector(self.x * other_coord, self.y * other_coord)

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

    def get_length(self: Vector) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self: Vector) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> float:
        degrees_angle = math.degrees(
            math.acos(
                (self * other) / (self.get_length() * other.get_length())
            )
        )
        return round(degrees_angle)

    def get_angle(self) -> float:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, angle: float) -> Vector:
        return Vector(
            self.x * math.cos(
                math.radians(angle)
            ) - self.y * math.sin(
                math.radians(angle)
            ),
            self.x * math.sin(
                math.radians(angle)
            ) + self.y * math.cos(
                math.radians(angle)
            )
        )
