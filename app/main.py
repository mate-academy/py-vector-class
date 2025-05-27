from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x_coord = round(x_coord, 2)
        self.y_coord = round(y_coord, 2)

    @property
    def x(self) -> float:
        return self.x_coord

    @property
    def y(self) -> float:
        return self.y_coord

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x_coord + other.x_coord,
            self.y_coord + other.y_coord,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x_coord - other.x_coord,
            self.y_coord - other.y_coord,
        )

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x_coord * other.x_coord + self.y_coord * other.y_coord
        return Vector(
            round(self.x_coord * other, 2),
            round(self.y_coord * other, 2),
        )

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float],
    ) -> Vector:
        x_coord = round(end_point[0] - start_point[0], 2)
        y_coord = round(end_point[1] - start_point[1], 2)
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return (self.x_coord ** 2 + self.y_coord ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length > 0:
            x_coord = self.x_coord / length
            y_coord = self.y_coord / length
            return Vector(x_coord, y_coord)
        return Vector(0, 0)

    def angle_between(self, other: Vector) -> float:
        dot = self * other
        lengths = self.get_length() * other.get_length()
        if lengths == 0:
            return 0
        cos_a = max(min(dot / lengths, 1), -1)
        angle_rad = math.acos(cos_a)
        return int(round(math.degrees(angle_rad)))

    def get_angle(self) -> float:
        if self.x_coord == 0 and self.y_coord == 0:
            return 0
        angle_rad = math.atan2(self.x_coord, self.y_coord)
        angle_deg = math.degrees(angle_rad)
        angle_clockwise = (360 - angle_deg) % 360
        return int(round(angle_clockwise))

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        x_coord = (
            self.x_coord * math.cos(radians) - self.y_coord * math.sin(radians)
        )
        y_coord = (
            self.x_coord * math.sin(radians) + self.y_coord * math.cos(radians)
        )
        return Vector(round(x_coord, 2), round(y_coord, 2))
