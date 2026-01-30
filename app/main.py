from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(round(self.x + other.x, 2), round(self.y + other.y, 2))

    def __sub__(self, other: Vector) -> Vector:
        return Vector(round(self.x - other.x, 2), round(self.y - other.y, 2))

    def __mul__(self, other: int | float | Vector) -> int | float | Vector:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            x_coord=round(end_point[0] - start_point[0], 2),
            y_coord=round(end_point[1] - start_point[1], 2)
        )

    def get_length(self) -> int | float:
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> Vector:
        return Vector(
            x_coord=round(self.x / self.get_length(), 2),
            y_coord=round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other: Vector) -> int:
        dot = self * other
        len_self = self.get_length()
        len_other = other.get_length()

        cos_a = dot / (len_self * len_other)

        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        radian = math.radians(degrees)

        return Vector(
            x_coord=round(
                self.x * math.cos(radian) - self.y * math.sin(radian), 2
            ),
            y_coord=round(
                self.x * math.sin(radian) + self.y * math.cos(radian), 2
            )
        )
