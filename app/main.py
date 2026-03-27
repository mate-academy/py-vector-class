from __future__ import annotations
from math import pi, acos, cos, sin, radians


class Vector:
    def __init__(
        self,
        x_coordinates: int | float,
        y_coordinates: int | float
    ) -> None:
        self.x = round(x_coordinates, 2)
        self.y = round(y_coordinates, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        raise TypeError("Invalid type")

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[int | float, int | float],
        end_point: tuple[int | float, int | float]
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ZeroDivisionError("Cannot normalize a zero vector")
        return Vector(self.x / length, self.y / length)

    def radian_angle_between(self, other: Vector) -> float:
        if not isinstance(other, Vector):
            raise TypeError("Invalid type")

        magnitudes_product = self.get_length() * other.get_length()
        if magnitudes_product == 0:
            return 0.0

        return acos((self * other) / magnitudes_product)

    def angle_between(self, other: Vector) -> int:
        return round(self.radian_angle_between(other) * (180 / pi))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: int) -> Vector:
        theta = radians(angle)
        new_x = round(self.x * cos(theta) - self.y * sin(theta), 2)
        new_y = round(self.x * sin(theta) + self.y * cos(theta), 2)
        return Vector(new_x, new_y)
