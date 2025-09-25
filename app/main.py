from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coordinate: int
                 | float, y_coordinate: int | float) -> None:

        self.x_coordinate = round(x_coordinate, 2)
        self.y_coordinate = round(y_coordinate, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(
                self.x_coordinate + other.x_coordinate,
                self.y_coordinate + other.y_coordinate,
            )
        return NotImplemented

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(
                self.x_coordinate - other.x_coordinate,
                self.y_coordinate - other.y_coordinate,
            )
        return NotImplemented

    def __mul__(self, other: int | float | "Vector") -> int | float | "Vector":
        if isinstance(other, (int | float)):
            return Vector(self.x_coordinate * other, self.y_coordinate * other)
        if isinstance(other, Vector):
            return (self.x_coordinate * other.x_coordinate) + (
                self.y_coordinate * other.y_coordinate
            )
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        x_coordinate = end_point[0] - start_point[0]
        y_coordinate = end_point[1] - start_point[1]
        return cls(x_coordinate, y_coordinate)

    def get_length(self) -> float:
        return math.sqrt(self.x_coordinate**2 + self.y_coordinate**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(
            round(self.x_coordinate / length, 2)
            , round(self.y_coordinate / length, 2)
        )

    def angle_between(self, other: "Vector") -> int | float:
        dot = (
            self.x_coordinate * other.x_coordinate
            + self.y_coordinate * other.y_coordinate
        )
        mag_self = math.sqrt(self.x_coordinate**2 + self.y_coordinate**2)
        mag_other = math.sqrt(other.x_coordinate**2 + other.y_coordinate**2)
        cos_a = dot / (mag_self * mag_other)
        cos_a = max(min(cos_a, 1), -1)
        angle_deg = math.degrees(math.acos(cos_a))
        return round(angle_deg)

    def get_angle(self) -> int | float:
        y_axis = Vector(0, 1)
        dot = (
            self.x_coordinate * y_axis.x_coordinate
            + self.y_coordinate * y_axis.y_coordinate
        )
        mag_self = math.sqrt(self.x_coordinate**2 + self.y_coordinate**2)
        mag_y = 1
        cos_a = dot / (mag_self * mag_y)
        cos_a = max(min(cos_a, 1), -1)
        angle_deg = math.degrees(math.acos(cos_a))
        return round(angle_deg)

    def rotate(self, degrees: int | float) -> int | float:
        radians = math.radians(degrees)
        new_x = self.x_coordinate * math.cos(
            radians) - self.y * math.sin(radians)
        new_y = self.x_coordinate * math.sin(
            radians) + self.y * math.cos(radians)
        return Vector(round(new_x, 2), round(new_y, 2))
