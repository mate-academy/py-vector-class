from __future__ import annotations
from math import sqrt, acos, degrees, radians, cos, sin


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x + other.x,
            y_coord=self.y + other.y,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x - other.x,
            y_coord=self.y - other.y,
        )

    def __mul__(self, other: int | float | Vector) -> int | float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            x_coord=self.x * other,
            y_coord=self.y * other,
        )

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[int | float, int | float],
        end_point: tuple[int | float, int | float],
    ) -> Vector:
        return cls(
            x_coord=end_point[0] - start_point[0],
            y_coord=end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(
            x_coord=self.x / length,
            y_coord=self.y / length,
        )

    def angle_between(self, other: Vector) -> int:
        len_self = self.get_length()
        len_other = other.get_length()
        if len_self == 0 or len_other == 0:
            return 0
        cos_theta = (self * other) / (len_self * len_other)
        cos_theta = max(-1.0, min(1.0, cos_theta))  # Clamp
        theta_radians = acos(cos_theta)
        return round(degrees(theta_radians))

    def get_angle(self) -> int:
        # Ângulo em relação ao eixo Y positivo
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees_angle: float | int) -> Vector:
        theta = radians(degrees_angle)
        return Vector(
            x_coord=self.x * cos(theta) - self.y * sin(theta),
            y_coord=self.x * sin(theta) + self.y * cos(theta)
        )

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"
