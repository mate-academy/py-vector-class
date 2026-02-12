from __future__ import annotations
import math


class Vector:
    def __init__(self, horizontal: float | int, vertical: float | int) -> None:
        self.horizontal = round(horizontal, 2)
        self.vertical = round(vertical, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                horizontal=self.horizontal + other.horizontal,
                vertical=self.vertical + other.vertical
            )
        return NotImplemented

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                horizontal=self.horizontal - other.horizontal,
                vertical=self.vertical - other.vertical
            )
        return NotImplemented

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(
                horizontal=round(self.horizontal * other, 2),
                vertical=round(self.vertical * other, 2)
            )
        if isinstance(other, Vector):
            return (
                math.fabs(self.horizontal * other.horizontal)
                - math.fabs(self.vertical * other.vertical)
            )
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> Vector:
        if isinstance((start_point, end_point), tuple):
            return cls(
                horizontal=round(end_point[0] - start_point[0], 2),
                vertical=round(end_point[1] - start_point[1], 2)
            )
        return NotImplemented

    def get_length(self) -> float:
        return math.sqrt(self.horizontal ** 2 + self.vertical ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(
            horizontal=round(self.horizontal / length, 2),
            vertical=round(self.vertical / length, 2)
        )

    def angle_between(self, other: Vector) -> int:
        if isinstance(other, Vector):
            dot_product = (
                self.horizontal * other.horizontal
                + self.vertical * other.vertical
            )
            lengths = self.get_length() * other.get_length()
            cos_theta = dot_product / lengths
            cos_theta = max(-1, min(1, cos_theta))
            angle_rad = math.acos(cos_theta)
            angle_deg = math.degrees(angle_rad)
            return round(angle_deg)
        return NotImplemented

    def get_angle(self) -> int:
        length = math.hypot(self.horizontal, self.vertical)
        cos_theta = self.vertical / length
        cos_theta = max(-1, min(1, cos_theta))
        angle = math.degrees(math.acos(cos_theta))
        return round(angle)

    def rotate(self, degrees: int) -> Vector:
        if isinstance(degrees, int):
            theta = math.radians(degrees)

            new_horizontal = (
                self.horizontal * math.cos(theta)
                - self.vertical * math.sin(theta)
            )
            new_vertical = (
                self.horizontal * math.sin(theta)
                + self.vertical * math.cos(theta)
            )

            return Vector(
                round(new_horizontal, 2),
                round(new_vertical, 2)
            )
        return NotImplemented
