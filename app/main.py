from __future__ import annotations
from typing import Self, Any
import math


class Point:
    def __init__(self, x: float, y: float) -> None:  # noqa: VNE001
        self.x = x
        self.y = y


class Vector:

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: Point,
            end_point: Point
    ) -> "Vector":
        x1, y1 = start_point
        x2, y2 = end_point
        return cls(x2 - x1, y2 - y1)

    def rotate(self, degrees: int | float) -> None:
        rad = math.radians(degrees)
        new_x = self.x * math.cos(rad) - self.y * math.sin(rad)
        new_y = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector(new_x, new_y)

    def __init__(self, x: int, y: int) -> None:  # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __sub__(self, other: Self) -> Self:
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> Self:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError(
                f"unsupported operand type(s) for *:"
                f" 'Vector' and '{type(other).__name__}'"
            )

    def __neg__(self) -> Self:
        return Vector(-self.x, -self.y)

    def __add__(self, other: Any) -> "Point":
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __abs__(self) -> float:
        return self.get_length()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: object) -> bool:
        return not self == other

    def get_length(self) -> int:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> int:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Point") -> float:
        if not isinstance(other, Vector):
            raise TypeError("angle_between expects a Vector")
        len_self = self.get_length()
        len_other = other.get_length()
        prod = len_self * len_other
        if prod == 0:
            return 0
        dot = self * other
        cos_a = dot / prod
        cos_a = max(-1.0, min(1.0, cos_a))
        angle_deg = int(round(math.degrees(math.acos(cos_a))))
        return angle_deg

    def get_angle(self) -> float:
        theta = math.degrees(math.atan2(self.y, self.x))
        angle_x = math.degrees(math.atan2(self.y, self.x))  # noqa: VNE001ret
        angle = (270 + theta) % 360
        return int(round(angle))
