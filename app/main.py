from __future__ import annotations

import math


class Vector:
    def __init__(self, x: float, y: float) -> None:   # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )

    def __mul__(
        self,
        other: Vector | int | float,
    ) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(
            self.x * other,
            self.y * other,
        )

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float],
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return math.sqrt(
            self.x ** 2 + self.y ** 2,
        )

    def get_normalized(self) -> Vector:
        length = self.get_length()

        return Vector(
            self.x / length,
            self.y / length,
        )

    def angle_between(self, vector: Vector) -> int:
        cos_a = (
            self * vector
        ) / (
            self.get_length()
            * vector.get_length()
        )

        return round(
            math.degrees(
                math.acos(cos_a),
            ),
        )

    def get_angle(self) -> int:
        return abs(
            round(
                math.degrees(
                    math.atan2(self.x, self.y)
                )
            )
        )

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)

        x = (self.x * math.cos(radians)  # noqa: VNE001
             - self.y * math.sin(radians))

        y = (self.x * math.sin(radians)  # noqa: VNE001
             + self.y * math.cos(radians))

        return Vector(x, y)
