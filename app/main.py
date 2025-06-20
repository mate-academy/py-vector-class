from __future__ import annotations
import math
from typing import Tuple, Union


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x_coordinate = round(x_coordinate, 2)
        self.y_coordinate = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError("Can only add Vector to Vector")
        return Vector(
            self.x_coordinate + other.x_coordinate,
            self.y_coordinate + other.y_coordinate
        )

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError("Can only subtract Vector from Vector")
        return Vector(
            self.x_coordinate - other.x_coordinate,
            self.y_coordinate - other.y_coordinate
        )

    def __mul__(self, other: Union[float, Vector]) -> Union[Vector, float]:
        if isinstance(other, (int, float)):
            return Vector(
                round(self.x_coordinate * other, 2),
                round(self.y_coordinate * other, 2)
            )
        elif isinstance(other, Vector):
            return (self.x_coordinate * other.x_coordinate
                    + self.y_coordinate * other.y_coordinate)
        raise TypeError("Can only multiply by number or Vector")

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: Tuple[float, float],
        end_point: Tuple[float, float]
    ) -> Vector:
        x_coordinate = end_point[0] - start_point[0]
        y_coordinate = end_point[1] - start_point[1]
        return cls(x_coordinate, y_coordinate)

    def get_length(self) -> float:
        return math.sqrt(self.x_coordinate ** 2 + self.y_coordinate ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x_coordinate / length, self.y_coordinate / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        magnitude_product = self.get_length() * other.get_length()
        if magnitude_product == 0:
            return 0
        cos_angle = dot_product / magnitude_product
        cos_angle = max(-1, min(1, cos_angle))
        angle_rad = math.acos(cos_angle)
        return round(math.degrees(angle_rad))

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        dot_product = self * y_axis
        magnitude_product = self.get_length() * y_axis.get_length()

        if magnitude_product == 0:
            return 0

        cos_angle = dot_product / magnitude_product
        cos_angle = max(-1, min(1, cos_angle))
        angle_rad = math.acos(cos_angle)
        angle_deg = math.degrees(angle_rad)

        if self.x_coordinate < 0:
            angle_deg = 360 - angle_deg

        return round(angle_deg)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos = math.cos(radians)
        sin = math.sin(radians)
        new_x = self.x_coordinate * cos - self.y_coordinate * sin
        new_y = self.x_coordinate * sin + self.y_coordinate * cos
        return Vector(round(new_x, 2), round(new_y, 2))

    def __repr__(self) -> str:
        return f"Vector({self.x_coordinate}, {self.y_coordinate})"
