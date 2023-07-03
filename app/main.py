from __future__ import annotations
import math


class Vector:
    def __init__(
            self,
            x_axis: float,
            y_axis: float
    ) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector) -> float | Vector:
        if type(other) == Vector:
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start: tuple,
            end: tuple
    ) -> Vector:
        return Vector(end[0] - start[0], end[1] - start[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        new_x = round(self.x / length, 2)
        new_y = round(self.y / length, 2)
        return Vector(new_x, new_y)

    def angle_between(self, other: Vector) -> float:
        mult = self * other
        length_first = self.get_length()
        length_second = other.get_length()
        cos_a = mult / (length_first * length_second)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return int(
            self.angle_between(
                Vector.create_vector_by_two_points((0, 0), (0, 5))
            )
        )

    def rotate(self, degrees: int) -> Vector:
        rad_degrees = math.radians(degrees)
        x_2 = math.cos(rad_degrees) * self.x - math.sin(rad_degrees) * self.y
        y_2 = math.sin(rad_degrees) * self.x + math.cos(rad_degrees) * self.y
        return Vector(x_2, y_2)
