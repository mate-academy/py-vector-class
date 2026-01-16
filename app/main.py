from __future__ import annotations

from math import sqrt, degrees, acos, cos, sin, radians


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(
                self.x * other,
                self.y * other
            )
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            round(end_point[0] - start_point[0], 2),
            round(end_point[1] - start_point[1], 2)
        )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        vector1_length = self.get_length()
        vector2_length = other.get_length()
        angle = degrees(acos(dot_product / (vector1_length * vector2_length)))

        return round(angle)

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees_to_rotate: int) -> Vector:
        deg_to_rad = radians(degrees_to_rotate)
        return Vector(
            self.x * cos(deg_to_rad) - self.y * sin(deg_to_rad),
            self.x * sin(deg_to_rad) + self.y * cos(deg_to_rad)
        )
