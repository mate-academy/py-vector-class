from __future__ import annotations
import math


class Vector:

    def __init__(self, x: int | float, y: int | float) -> None:  # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(
                self.x + other.x,
                self.y + other.y,
            )
        return NotImplemented

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(
                self.x - other.x,
                self.y - other.y,
            )
        return NotImplemented

    def __mul__(self, other: int | float | "Vector") -> int | float | "Vector":
        if isinstance(other, (int | float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return (self.x * other.x) + (
                self.y * other.y
            )
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        x_coord = end_point[0] - start_point[0]
        y_coord = end_point[1] - start_point[1]
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(
            round(self.x / length, 2)
            , round(self.y / length, 2)
        )

    def angle_between(self, other: "Vector") -> int | float:
        dot = (
            self.x * other.x
            + self.y * other.y
        )
        mag_self = math.sqrt(self.x**2 + self.y**2)
        mag_other = math.sqrt(other.x**2 + other.y**2)
        cos_a = dot / (mag_self * mag_other)
        cos_a = max(min(cos_a, 1), -1)
        angle_deg = math.degrees(math.acos(cos_a))
        return round(angle_deg)

    def get_angle(self) -> int | float:
        y_axis = Vector(0, 1)
        dot = (
            self.x * y_axis.x
            + self.y * y_axis.y
        )
        mag_self = math.sqrt(self.x**2 + self.y**2)
        mag_y = 1
        cos_a = dot / (mag_self * mag_y)
        cos_a = max(min(cos_a, 1), -1)
        angle_deg = math.degrees(math.acos(cos_a))
        return round(angle_deg)

    def rotate(self, degrees: int | float) -> int | float:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(
            radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(
            radians) + self.y * math.cos(radians)
        return Vector(round(new_x, 2), round(new_y, 2))
