from __future__ import annotations
import math
from decimal import Decimal, ROUND_HALF_UP


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x_coordinate = float(
            Decimal(x_coordinate).quantize(
                Decimal("0.01"), rounding=ROUND_HALF_UP
            )
        )
        self.y_coordinate = float(
            Decimal(y_coordinate).quantize(
                Decimal("0.01"), rounding=ROUND_HALF_UP
            )
        )

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x_coordinate + other.x_coordinate,
            self.y_coordinate + other.y_coordinate,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x_coordinate - other.x_coordinate,
            self.y_coordinate - other.y_coordinate,
        )

    def __mul__(self, other: int | float | Vector) -> Vector | int | float:
        if isinstance(other, (int, float)):
            return Vector(
                self.x_coordinate * other,
                self.y_coordinate * other,
            )
        elif isinstance(other, Vector):
            return (
                self.x_coordinate * other.x_coordinate
                + self.y_coordinate * other.y_coordinate
            )
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return math.sqrt(
            self.x_coordinate**2 + self.y_coordinate**2
        )

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(
            self.x_coordinate / length,
            self.y_coordinate / length,
        )

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        lengths_product = self.get_length() * other.get_length()
        if lengths_product == 0:
            return 0
        cos_angle = max(-1, min(1, dot_product / lengths_product))
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = (
            self.x_coordinate * math.cos(radians)
            - self.y_coordinate * math.sin(radians)
        )
        new_y = (
            self.x_coordinate * math.sin(radians)
            + self.y_coordinate * math.cos(radians)
        )
        return Vector(new_x, new_y)

    def __repr__(self) -> str:
        return (
            f"Vector({self.x_coordinate}, {self.y_coordinate})"
        )
