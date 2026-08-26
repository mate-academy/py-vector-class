from __future__ import annotations

from math import sqrt, degrees, acos, radians, cos, sin


class Vector:
    def __init__(self, x_input: int | float, y_input: int | float) -> None:
        self.x = round(x_input, 2)
        self.y = round(y_input, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                self.x + other.x,
                self.y + other.y
            )
        else:
            return NotImplemented

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                self.x - other.x,
                self.y - other.y
            )
        else:
            return NotImplemented

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, (int, float)):
            return Vector(
                self.x * other,
                self.y * other
            )
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return NotImplemented

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float | int:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> float | int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(degrees(acos(cos_a)))

    def get_angle(self) -> float | int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degree: float | int) -> Vector:
        rad = radians(degree)
        new_x = self.x * cos(rad) - self.y * sin(rad)
        new_y = self.x * sin(rad) + self.y * cos(rad)
        return Vector(new_x, new_y)
