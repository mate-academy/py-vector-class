from __future__ import annotations
import math


class Vector:
    def __init__(self, x_val: float, y_val: float) -> None:
        self.x = round(x_val, 2)
        self.y = round(y_val, 2)

    @staticmethod
    def is_valid_type(other: Vector) -> None:
        if not isinstance(other, Vector):
            raise TypeError(f"Unsupported operand type {type(other)}")

    def __add__(self, other: Vector) -> Vector:
        self.is_valid_type(other)
        return Vector(
            x_val=self.x + other.x,
            y_val=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        self.is_valid_type(other)
        return Vector(
            x_val=self.x - other.x,
            y_val=self.y - other.y
        )

    def __mul__(self, other: Vector | float) -> Vector | float:
        if not isinstance(other, (Vector, float, int)):
            raise TypeError(f"Unsupported operand type {type(other)}")
        if type(other) in (float, int):
            return Vector(
                x_val=other * self.x,
                y_val=other * self.y
            )
        return other.x * self.x + other.y * self.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float],
            end_point: tuple[float]
    ) -> Vector:
        return cls(
            x_val=end_point[0] - start_point[0],
            y_val=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            x_val=self.x / self.get_length(),
            y_val=self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        cos_a = (self.x * other.x + self.y * other.y) / \
                (self.get_length() * other.get_length())

        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> Vector:
        cos_a = math.cos(math.radians(degrees))
        sin_a = math.sin(math.radians(degrees))
        return Vector(
            x_val=self.x * cos_a - self.y * sin_a,
            y_val=self.y * cos_a + self.x * sin_a
        )

    def get_angle(self) -> int:
        cos_a = (self.y * self.y) / (self.get_length() * self.y)

        return round(math.degrees(math.acos(cos_a)))
