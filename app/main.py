from __future__ import annotations
import math


class Vector:
    def __init__(self, x_value: int | float, y_value: int | float) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | int | Vector) -> Vector | int | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(round((self.x * other), 2), round((self.y * other), 2))

    @classmethod
    def create_vector_by_two_points(
            cls: Vector,
            start_point: set,
            end_point: set
    ) -> Vector:
        return Vector(
            round(end_point[0] - start_point[0], 2),
            round(end_point[1] - start_point[1], 2)
        )

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )

    def angle_between(self, vektor: Vector) -> int:
        cos_alpha = self * vektor / (self.get_length() * vektor.get_length())
        return round(math.degrees(math.acos(cos_alpha)))

    def get_angle(self) -> int:
        angle_rad = math.atan2(self.x, self.y)
        angle_degrees = math.degrees(angle_rad)
        if angle_degrees < 0:
            angle_degrees = abs(angle_degrees)
        return round(angle_degrees)

    def rotate(self, degrees: int) -> Vector:
        phi = math.radians(degrees)
        prev_x = self.x
        prev_y = self.y
        new_x = prev_x * math.cos(phi) - prev_y * math.sin(phi)
        new_y = prev_x * math.sin(phi) + prev_y * math.cos(phi)
        return Vector(new_x, new_y)
