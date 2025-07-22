from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple[float], end_point: tuple[float]
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return self * (1 / self.get_length())

    def angle_between(self, other: Vector) -> float:
        return round(
            math.degrees(
                math.acos(
                    self * other / self.get_length() / other.get_length()
                )
            )
        )

    def get_angle(self) -> int:
        res = abs(round(math.degrees(math.atan(self.x / self.y))))
        return 180 - res if self.y < 0 else res

    def rotate(self, angle: int) -> Vector:
        return Vector(
            round(
                math.cos(math.radians(angle)) * self.x
                - math.sin(math.radians(angle)) * self.y,
                2
            ),
            round(
                math.sin(math.radians(angle)) * self.x
                + math.cos(math.radians(angle)) * self.y,
                2
            )
        )
