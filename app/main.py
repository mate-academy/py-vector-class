from __future__ import annotations
import math


class Vector:

    def __init__(self, axis_x: float, axis_y: float) -> None:
        self.x = round(axis_x, 2)
        self.y = round(axis_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            axis_x=self.x + other.x,
            axis_y=self.y + other.y
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            axis_x=self.x - other.x,
            axis_y=self.y - other.y
        )

    def __mul__(self, other: "Vector" | int) -> "Vector" | float:
        if not isinstance(other, Vector):
            return Vector(
                axis_x=self.x * other,
                axis_y=self.y * other
            )

        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def get_normalized(self) -> "Vector":
        return Vector(
            axis_x=self.x / self.get_length(),
            axis_y=self.y / self.get_length()
        )

    def angle_between(self, other: "Vector") -> int:
        scalar_product = self * other
        mods_product = self.get_length() * other.get_length()
        cos = scalar_product / mods_product
        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> int:
        return abs(
            round(
                math.degrees(math.atan2(self.x, self.y))
            )
        )

    def rotate(self, degrees: int) -> "Vector":
        angle_rad = math.radians(degrees)
        new_x = self.x * math.cos(angle_rad) - self.y * math.sin(angle_rad)
        new_y = self.x * math.sin(angle_rad) + self.y * math.cos(angle_rad)
        return Vector(new_x, new_y)
