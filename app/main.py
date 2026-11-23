from __future__ import annotations
import math


class Vector:
    def __init__(
            self,
            value_x: float | int,
            value_y: float | int
    ) -> None:
        self.x = round(value_x, 2)
        self.y = round(value_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | int | Vector) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        scalar_product = self * other
        length = self.get_length() * other.get_length()
        return round(
            math.degrees(
                math.acos(
                    min(1, max(-1, scalar_product / length))
                )
            )
        )

    def get_angle(self) -> int:
        return round(
            math.degrees(
                math.acos(
                    min(1, max(-1, self.y / self.get_length()))
                )
            )
        )

    def rotate(self, degrees: int) -> Vector:
        degrees_rad = math.radians(degrees)
        return Vector(
            self.x * math.cos(degrees_rad) - self.y * math.sin(degrees_rad),
            self.x * math.sin(degrees_rad) + self.y * math.cos(degrees_rad)
        )
