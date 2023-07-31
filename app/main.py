from __future__ import annotations
import math


class Vector:
    def __init__(self, x_axis: float, y_axis: float) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_axis=self.x + other.x,
            y_axis=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_axis=self.x - other.x,
            y_axis=self.y - other.y
        )

    def __mul__(self, other: float) -> float | Vector:
        if not isinstance(other, Vector):
            return Vector(
                x_axis=self.x * other,
                y_axis=self.y * other
            )
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> Vector:
        return Vector(
            x_axis=end_point[0] - start_point[0],
            y_axis=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        return Vector(
            x_axis=self.x / self.get_length(),
            y_axis=self.y / self.get_length()
        )

    def angle_between(self, vector: Vector) -> int:
        dot_product = (self.x * vector.x) + (self.y * vector.y)
        mag1 = self.get_length()
        mag2 = vector.get_length()
        return round(math.degrees(math.acos(dot_product / (mag1 * mag2))))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        degrees = math.radians(degrees)
        return Vector(
            x_axis=(math.cos(degrees) * self.x) - (math.sin(degrees) * self.y),
            y_axis=(math.sin(degrees) * self.x) + (math.cos(degrees) * self.y)
        )
