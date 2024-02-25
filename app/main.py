from __future__ import annotations
import math


class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x=self.x - other.x, y=self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        """
        Multiplying Vector on a number return another Vector.
        Multiplying Vector on Vector should their dot product.
        """

        if isinstance(other, (int, float)):
            return Vector(x=self.x * other, y=self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        x_1, y_1 = start_point
        x_2, y_2 = end_point
        return cls(x=(x_2 - x_1), y=(y_2 - y_1))

    def get_length(self) -> int | float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(x=round(self.x / length, 2), y=round(self.y / length, 2))

    def angle_between(self, other: Vector) -> int:
        """Angle between 2 vectors"""
        return round(
            math.degrees(
                math.acos(
                    (self * other) / (self.get_length() * other.get_length())
                )
            )
        )

    def get_angle(self) -> int:
        """Angle between current vector and positive Y axis"""
        return self.angle_between(Vector(x=0, y=1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(
            x=math.cos(radians) * self.x - math.sin(radians) * self.y,
            y=math.sin(radians) * self.x + math.cos(radians) * self.y,
        )
